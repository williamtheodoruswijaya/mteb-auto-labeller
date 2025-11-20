import requests
import csv
import time
import re
import pandas as pd

URL_DAFTAR_LAPORAN = "https://crm.jakarta.go.id/api/public/dashboard/distribution-map?dateStart=2024-11-01&dateEnd=2025-07-23&zoneId=&isPrivacy=0"
URL_DETAIL_LAPORAN = "https://crm.jakarta.go.id/api/public/dashboard/detail?id={id}"
NAMA_FILE_CSV = "dataset_laporan_crm_untuk_triase.csv"
HEADERS = [
    'id', 'code', 'content', 'image_url', 'latitude', 'longitude',
    'status', 'category', 'zone', 'village', 'district', 'city', 'province', 'created_at'
]

def extract_permasalahan_robust(full_content: str) -> str:
    if not isinstance(full_content, str):
        return ""
    pattern = re.compile(r'Permasalahan:\s*(.*?)\s*(?:Kategori:|Lokasi:|Detail Alamat Laporan:|$)', re.DOTALL)
    
    match = pattern.search(full_content)
    
    if match:
        return match.group(1).strip()
    else:
        return " ".join(full_content.replace("Permasalahan:", "").split())

def scrape_laporan_crm():
    print(f"Memulai proses scraping dan menyimpan ke '{NAMA_FILE_CSV}'...")
    with open(NAMA_FILE_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADERS)

        total_laporan_sukses = 0
        total_laporan_gagal = 0

        try:
            print("Mengambil daftar semua laporan dari API...")
            response_list = requests.get(URL_DAFTAR_LAPORAN, timeout=60)
            response_list.raise_for_status()
            daftar_laporan = response_list.json()

            if not daftar_laporan or not isinstance(daftar_laporan, list):
                print("API tidak mengembalikan daftar laporan yang valid. Proses berhenti.")
                return

            print(f"Berhasil mendapatkan {len(daftar_laporan)} total laporan. Memulai proses detail...")

            for item in daftar_laporan:
                laporan_id = item.get('id')
                if not laporan_id:
                    continue

                try:
                    response_detail = requests.get(URL_DETAIL_LAPORAN.format(id=laporan_id), timeout=30)
                    if 400 <= response_detail.status_code < 500:
                        total_laporan_gagal += 1
                        continue
                    response_detail.raise_for_status()
                    detail_laporan = response_detail.json()

                    documents = detail_laporan.get('documents', [])
                    image_url = documents[0].get('url') if documents and isinstance(documents, list) else None
                    zone_name = (item.get('zone') or {}).get('name')

                    if not zone_name:
                        total_laporan_gagal += 1
                        continue

                    raw_content = item.get('content', '')
                    cleaned_content = extract_permasalahan_robust(raw_content)

                    village_data = detail_laporan.get('village', {}) or {}
                    district_data = village_data.get('district', {}) or {}
                    city_data = district_data.get('city', {}) or {}
                    province_data = city_data.get('province', {}) or {}

                    row_data = [
                        laporan_id,
                        item.get('code'),
                        cleaned_content,
                        image_url,
                        item.get('lat'),
                        item.get('lng'),
                        (item.get('tstatus') or {}).get('name'),
                        (item.get('complaintCategory') or {}).get('name'),
                        zone_name,
                        village_data.get('name'),
                        district_data.get('name'),
                        city_data.get('name'),
                        province_data.get('name'),
                        item.get('createdAt')
                    ]

                    writer.writerow(row_data)
                    total_laporan_sukses += 1

                except requests.exceptions.RequestException as e:
                    print(f"❌ Error saat mengambil detail untuk ID {laporan_id}: {e}")
                    total_laporan_gagal += 1
                except Exception as e:
                    print(f"❌ Error saat memproses data untuk ID {laporan_id}: {e}")
                    total_laporan_gagal += 1

                time.sleep(0.1)

        except requests.exceptions.RequestException as e:
            print(f"❌ Gagal mengambil daftar laporan utama. Error: {e}")
        except ValueError:
            print("❌ Gagal mem-parsing JSON dari daftar laporan utama.")

    print("Proses scraping selesai!")
    print(f"Total laporan berhasil disimpan: {total_laporan_sukses}")
    print(f"Total laporan gagal/dilewati: {total_laporan_gagal}")
    print(f"Dataset disimpan di file: '{NAMA_FILE_CSV}'")

    print("\nAnalisis Awal Distribusi UKPD Penanggung Jawab (kolom 'zone'):")
    try:
        df = pd.read_csv(NAMA_FILE_CSV)
        zone_counts = df['zone'].value_counts()
        print(zone_counts)
    except FileNotFoundError:
        print("File CSV tidak ditemukan, analisis distribusi dibatalkan.")

if __name__ == "__main__":
    scrape_laporan_crm()
