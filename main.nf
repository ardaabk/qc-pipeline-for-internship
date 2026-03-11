nextflow.enable.dsl=2

params.reads = "barcode77.fastq"
params.outdir = "results"

process NANOPLOT_QC {
    publishDir "${params.outdir}/nanoplot", mode: 'copy'

    input:
    path fastq

    output:
    path "*"

    script:
    """
    NanoPlot --fastq "${fastq}" -o .
    """
}

process CUSTOM_PIPELINE {
    publishDir "${params.outdir}/custom_qc", mode: 'copy'

    input:
    path fastq

    output:
    path "*_metrics.csv"
    path "*_distributions.png"

    script:
    """
    python "${projectDir}/script.py" "${fastq}" read
    """
}

workflow {
    reads_ch = Channel.fromPath(params.reads)
    
    NANOPLOT_QC(reads_ch)
    CUSTOM_PIPELINE(reads_ch)
}