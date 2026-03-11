TR:
Long-Read QC Pipeline
Bu depo, uzun okuma (long-read) dizileme verileri için Nextflow ve Python kullanılarak hazırlanmış bir Kalite Kontrol (QC) iş akışını içermektedir.

Gereksinimler
Conda veya Miniconda
Nextflow

Nasıl Çalıştırılır?
1. Bu repoyu bilgisayarınıza klonlayın.
2. Gerekli araçların kurulması için Conda ortamını oluşturun ve aktif edin:
   bash
   conda env create -f environment.yml
   conda activate massive_qc_env
Ham fastq dosyanızı proje dizinine ekleyin (varsayılan: barcode77.fastq).

Pipeline'ı başlatın:

 nextflow run main.nf


İşlem tamamlandığında çıktılar results/ klasörü içerisine kaydedilecektir.



EN:
Long-Read QC Pipeline
This repository contains a Quality Control (QC) workflow for long-read sequencing data, developed using Nextflow and Python.

Prerequisites
Conda or Miniconda
Nextflow

How to Run? :
Clone this repository to your local machine.
Create and activate the Conda environment to install the required tools:
Bash
conda env create -f environment.yml
conda activate massive_qc_env

Add your raw fastq file to the project directory (default: barcode77.fastq).

Run the pipeline:
Bash
nextflow run main.nf
Once the process is complete, the outputs will be saved in the results/ folder.




