---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:39098
- loss:DenoisingAutoEncoderLoss
base_model: indobenchmark/indobert-base-p1
widget:
- source_sentence: siang perusahaan transportasi resiko laporan dipindah tempelan
    liar
  sentences:
  - selamat siang dicopot pelaku pengrusakan lapisan cat perusahaan transportasi online
    resiko laporan berulang dipindah posting tempelan banner rokok liar
  - pelanggaran parkir liar pkl samping jalan menganggu macet masuk arah season city
  - lampu pju mati tolong diperbaiki terang terimakasih
- source_sentence: jakarta lanjuti
  sentences:
  - butuh ditindaklanjuti menjelang ppdb sma rt rw masuk zonasi sma rt amp rw masuk
    zonasi
  - sampah komplek penanganan kebersihan ppsu klender jakarta timur tindak lanjuti
  - sampah berserakan mohon dibersihkan rutin disapu rutin lapor jaki
- source_sentence: pagar dicoret radikal dpt
  sentences:
  - vandalisme pagar dicoret coret radikal radikal tolong dpt dihapus
  - pembangunan taman yg memakan bahu jalan menyisakan akses pejalan kaki mohon ditinjau
    ulang sesuai kaidah peraturan yg berlaku membangun fasilitas trotoar pejalan kaki
    yg layak tertibkan bangunan bangun sungai
  - penuh sampah selokan nya butuh ditindaklanjuti banjir
- source_sentence: xl halte kehujanan bis mohon pasang
  sentences:
  - xl halte atap warga kehujanan menunggu bis mohon pasang halte
  - permasalahan permasalahan permainan anak taman buni rusak berbahaya diperbaiki
    mohon diperbaiki fasilitas kenyamanan warga anak anak mohon atensi suku dinas
    dinas terkait terima kasih
  - parkir liar mengganggu lintas lajur utk parkir
- source_sentence: siangkut estin les banner posting berulang diunjuk pajak
  sentences:
  - siangkut iklan reklame estin salon iklan les reklame mapan banner salon yg reklame
    instan resiko posting berulang diunjuk surat pajak kecuali dha bayar pajak pemasangan
    berlaku
  - selokan dangkal hujan air tertampung mohon dikeruk selokan
  - menindaklanjuti id laporan jk terimakasih bu hasil laporan maret maaf bu izin
    menanggapi darihasil laporan point i ii iii maret khawatir teguran dihari maret
    pemilik usaha mengungsikan karyawan menunda proses produksi tas takut pelaku usaha
    petugas tgl maret pelaku usaha menyewakan usaha permintaan maaf warga terkena
    dampak kpd yg letak rumahnya berdekatan penyampaian petugas maret dinas izin usaha
    melaporkan limbah dilaporan jk menyebut limbah pengaduan terkait pencemaran udara
    proses pengeleman lem latex yg pelaku usaha mengakui lem yg dibelinya yg murah
    bantahan limbah pelaku usaha yg menyewakan mengada bukti video penyampaian keluhan
    kpd pelaku usaha jg kirim link tsb komentar id jk upload pribadi youtube memudahkan
    share video mengumpulkan buktinya melaporkan ketidaksesuaian terimakasih bu respon
    tindak lanjuti
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on indobenchmark/indobert-base-p1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1) <!-- at revision c2cd0b51ddce6580eb35263b39b0a1e5fb0a39e2 -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'siangkut estin les banner posting berulang diunjuk pajak',
    'siangkut iklan reklame estin salon iklan les reklame mapan banner salon yg reklame instan resiko posting berulang diunjuk surat pajak kecuali dha bayar pajak pemasangan berlaku',
    'selokan dangkal hujan air tertampung mohon dikeruk selokan',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.7334,  0.1294],
#         [ 0.7334,  1.0000, -0.0451],
#         [ 0.1294, -0.0451,  1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 39,098 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                         |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             |
  | details | <ul><li>min: 3 tokens</li><li>mean: 10.88 tokens</li><li>max: 76 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 24.36 tokens</li><li>max: 128 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                             | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>butuh pemangkasan butuh ditindaklanjuti</code>                                                                                                                                                                                                                                                                                   | <code>pohon butuh pemangkasan penopingan pohon lebat terimakasih butuh ditindaklanjuti</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | <code>dipaksa perijinan pbb perrgub perijinan</code>                                                                                                                                                                                                                                                                                   | <code>dipaksa urus perijinan pbb imb tindak screenshot selesai budaya kerja tuntas perrgub dki nurut kemen pupr perijinan sesang bangunharus diunjuk</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | <code>kasudin satuan pelaksana kec sehubungan jl xxi nama warga rt rw cempaka eksisting pertimbangan trotoar eksisting rumah zona mendekati tikungan rawan kecelakaan lintas yg padat xxi blm shg rawan jambret kali disambungnya trotoar yg tsb diharapkan pejalan rw dpt nyaman harapan jakpus terima ketua rt ir tembusan rt</code> | <code>terhormat kasudin binamarga jakpus satuan pelaksana kec cempaka putih sehubungan pekerjaan normalisasi saluran air jl cpt xxi sisi timur aplikasi izinkan nama warga rt rw kel cempaka putih tim mengajukan permohonan perpanjangan trotoar eksisting pertigaan cpt xxvi meter pertimbangan sbb trotoar eksisting dilanjut pertigaan rumah zona mendekati tikungan parkir roda shg rawan kecelakaan pelanggaran parkir tikungan mengganggu lintas yg padat trotoar cpt xxi blm memadai shg pejalan kaki memanfaatkan bahu jalan berdampak rawan kecelakaan kejahatan jambret hp berulang kali jalan yg padat lalin disambungnya trotoar yg tsb diharapkan warga pejalan kaki rw dpt beraktivitas dgn aman amp nyaman harapan permohonan dpt dikabulkan sudin bina marga jakpus perhatian layanannya terima kasih ketua rt rw kel cempaka putih timur ir nurrachman st mm tembusan ketua rw ketua rt</code> |
* Loss: [<code>DenoisingAutoEncoderLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#denoisingautoencoderloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 5
- `fp16`: True
- `disable_tqdm`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 5
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: True
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step  | Training Loss |
|:------:|:-----:|:-------------:|
| 0.1023 | 500   | 6.6108        |
| 0.2046 | 1000  | 5.5857        |
| 0.3069 | 1500  | 5.1713        |
| 0.4092 | 2000  | 4.9339        |
| 0.5115 | 2500  | 4.739         |
| 0.6137 | 3000  | 4.6369        |
| 0.7160 | 3500  | 4.5536        |
| 0.8183 | 4000  | 4.4559        |
| 0.9206 | 4500  | 4.3928        |
| 1.0229 | 5000  | 4.2662        |
| 1.1252 | 5500  | 4.0103        |
| 1.2275 | 6000  | 3.9584        |
| 1.3298 | 6500  | 3.9533        |
| 1.4321 | 7000  | 3.8681        |
| 1.5344 | 7500  | 3.8676        |
| 0.1023 | 500   | 3.715         |
| 0.2046 | 1000  | 3.6732        |
| 0.3069 | 1500  | 3.704         |
| 0.4092 | 2000  | 3.6216        |
| 0.5115 | 2500  | 3.6639        |
| 0.6137 | 3000  | 3.6454        |
| 0.7160 | 3500  | 3.6397        |
| 0.8183 | 4000  | 3.6391        |
| 0.9206 | 4500  | 3.6689        |
| 1.0229 | 5000  | 3.5506        |
| 1.1252 | 5500  | 3.3284        |
| 1.2275 | 6000  | 3.3463        |
| 1.3298 | 6500  | 3.3668        |
| 1.4321 | 7000  | 3.3374        |
| 1.5344 | 7500  | 3.3231        |
| 1.6367 | 8000  | 3.3943        |
| 1.7390 | 8500  | 3.3297        |
| 1.8412 | 9000  | 3.3138        |
| 1.9435 | 9500  | 3.3654        |
| 2.0458 | 10000 | 3.1605        |
| 2.1481 | 10500 | 2.9747        |
| 2.2504 | 11000 | 3.0076        |
| 2.3527 | 11500 | 3.0063        |
| 2.4550 | 12000 | 2.9473        |
| 2.5573 | 12500 | 3.0181        |
| 2.6596 | 13000 | 3.0216        |
| 2.7619 | 13500 | 2.9408        |
| 2.8642 | 14000 | 3.013         |
| 2.9664 | 14500 | 2.9246        |
| 3.0687 | 15000 | 2.7772        |
| 3.1710 | 15500 | 2.7404        |
| 3.2733 | 16000 | 2.7064        |
| 3.3756 | 16500 | 2.7013        |
| 3.4779 | 17000 | 2.702         |
| 3.5802 | 17500 | 2.6754        |
| 3.6825 | 18000 | 2.6354        |
| 3.7848 | 18500 | 2.6533        |
| 3.8871 | 19000 | 2.6731        |
| 3.9894 | 19500 | 2.6333        |
| 4.0917 | 20000 | 2.5023        |
| 4.1939 | 20500 | 2.499         |
| 4.2962 | 21000 | 2.534         |
| 4.3985 | 21500 | 2.5126        |
| 4.5008 | 22000 | 2.5259        |
| 4.6031 | 22500 | 2.5281        |
| 4.7054 | 23000 | 2.5099        |
| 4.8077 | 23500 | 2.5534        |
| 4.9100 | 24000 | 2.5457        |


### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.1.2
- Transformers: 4.57.2
- PyTorch: 2.9.0+cu126
- Accelerate: 1.12.0
- Datasets: 4.0.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### DenoisingAutoEncoderLoss
```bibtex
@inproceedings{wang-2021-TSDAE,
    title = "TSDAE: Using Transformer-based Sequential Denoising Auto-Encoderfor Unsupervised Sentence Embedding Learning",
    author = "Wang, Kexin and Reimers, Nils and Gurevych, Iryna",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    pages = "671--688",
    url = "https://arxiv.org/abs/2104.06979",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->