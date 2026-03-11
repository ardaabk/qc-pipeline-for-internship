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