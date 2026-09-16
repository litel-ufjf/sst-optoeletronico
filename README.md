# Análise Optoeletrônica de Turbidez e SST (Sólidos Suspensos Totais)

Este projeto consiste em um pipeline de processamento de dados e análise exploratória para sensores optoeletrônicos de medição de turbidez e SST. O sistema analisa dados de fotodetectores posicionados a **90°** (espalhamento nefelométrico) e **135°** (retroespalhamento), avaliando a estabilidade do sensor e gerando curvas de calibração baseadas em sinais brutos e combinados.

---

## Arquitetura do Projeto

```text
.
├── data/
│   ├── processed/                # Dados consolidados em formato .parquet
│   │   └── dados_consolidados.parquet
│   └── raw/                      # Dados brutos coletados por dia e rodada
│       ├── 14-09-2026/
│       │   ├── 01/
│       │   │   ├── 1_4.txt
│       │   │   ├── 1_5.txt
│       │   │   ├── agua.txt
│       │   │   ├── sst.txt
│       │   │   └── vazio.txt
│       │   └── ...
│       └── 15-09-2026/
│           └── ...
├── figures/                      # Gráficos exportados pelos notebooks
│   ├── varredura/                # Séries temporais de estabilidade
│   └── calibracao/               # Boxplots e curvas de calibração
├── notebooks/
│   ├── 01_varredura.ipynb        # Análise de séries temporais e estabilidade
│   └── 02_calibracao.ipynb       # Curvas de calibração e fusão de sinais (90° + 135°)
├── .gitignore                    # Arquivos ignorados pelo Git
├── README.md                     # Documentação do projeto
├── requirements.txt              # Dependências do ambiente Python
└── run_batch_processing.py       # Script de ingestão e processamento em lote