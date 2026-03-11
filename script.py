import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import SeqIO

def calculate_mean_quality(quality_scores):
    if not quality_scores:
        return 0
    return sum(quality_scores) / len(quality_scores)

def main():
    input_fastq = sys.argv[1]
    output_prefix = sys.argv[2]
    output_csv = f"{output_prefix}_metrics.csv"

    print(f"[{input_fastq}] okunuyor ve metrikler hesaplanıyor...")
    
    # Verileri bir listede toplayalım
    data = []
    for record in SeqIO.parse(input_fastq, "fastq"):
        read_id = record.id
        length = len(record.seq)
        
        # GC oranı hesaplama
        g_count = record.seq.count('G') + record.seq.count('g')
        c_count = record.seq.count('C') + record.seq.count('c')
        gc_content = ((g_count + c_count) / length * 100) if length > 0 else 0
        
        # Kalite skoru hesaplama
        mean_q = calculate_mean_quality(record.letter_annotations["phred_quality"])
        
        data.append([read_id, length, gc_content, mean_q])

    # Veriyi Pandas formatına çevirip CSV olarak kaydet
    df = pd.DataFrame(data, columns=['Read_ID', 'Length', 'GC_Content', 'Mean_Quality'])
    df.to_csv(output_csv, index=False)
    print(f"Metrikler başarıyla kaydedildi: {output_csv}")

    # Özet istatistikleri terminale yazdır
    print("\n--- ÖZET İSTATİSTİKLER ---")
    for col in ['Length', 'GC_Content', 'Mean_Quality']:
        print(f"{col} -> Ortalama: {df[col].mean():.2f} | Ortanca: {df[col].median():.2f}")
    print("--------------------------\n")

    # Grafikleri Çiz
    print("Grafikler oluşturuluyor...")
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    sns.histplot(df['Length'], bins=50, kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title('Okuma Uzunluğu Dağılımı')
    axes[0].set_xlabel('Bç (bp)')

    sns.histplot(df['GC_Content'], bins=50, kde=True, ax=axes[1], color='lightgreen')
    axes[1].set_title('GC Oranı Dağılımı (%)')
    axes[1].set_xlabel('GC (%)')

    sns.histplot(df['Mean_Quality'], bins=50, kde=True, ax=axes[2], color='salmon')
    axes[2].set_title('Ortalama Kalite Skoru (Phred)')
    axes[2].set_xlabel('Kalite Skoru')

    plt.tight_layout()
    plot_file = f"{output_prefix}_distributions.png"
    plt.savefig(plot_file, dpi=300)
    print(f"Grafikler başarıyla kaydedildi: {plot_file}")

if __name__ == "__main__":
    main()