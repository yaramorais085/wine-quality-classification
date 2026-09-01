# 🍷 Predição da Qualidade de Vinhos com Machine Learning

Este repositório contém a solução do **Tech Challenge - Fase 2** da Pós-Graduação em Data Analytics (FIAP / Pós-Tech).  
O objetivo do projeto é desenvolver um modelo preditivo de classificação capaz de estimar a qualidade de um vinho com base em suas características físico-químicas laboratoriais, simplificando o problema em uma **classificação binária** para prever se um vinho é de **alta qualidade (nota ≥ 7)** ou **baixa/média qualidade (nota < 7)**.

---

## 📺 Entregáveis Executivos

O conteúdo sintetiza as dores identificadas, os dados analisados, os principais insights e as recomendações estratégicas relacionadas à qualidade dos vinhos. Os resultados foram organizados em gráficos e tabelas comparativas, com foco em **storytelling de negócios**.

* ▶️ **Vídeo da Apresentação Executiva (YouTube):** [Clique aqui para assistir ao vídeo](https://youtu.be/xj8ShE8fCOg)
* 📊 **Apresentação em Slides (PPTX / PDF):** [`presentation/Apresentacao_Executiva_Vinhos.pptx`](https://github.com/yaramorais085/wine-quality-classification/blob/main/presentation/Apresentacao_Executiva_Vinhos.pptx)
* 📓 **Jupyter Notebook Completo:** [`notebooks/TechChallengeVinho_Otimizado.ipynb`](https://github.com/yaramorais085/wine-quality-classification/blob/main/notebooks/TechChallengeVinho_Otimizado.ipynb)

---

## 🔍 Principais Insights da Análise Exploratória (EDA)

A base final conta com **1.018 amostras únicas** após o tratamento e remoção de 125 duplicidades.

1. **Desbalanceamento Severo:** Vinhos de alta qualidade representam apenas **~13,5%** da base (137 amostras), enquanto vinhos comuns representam **86,5%** (881 amostras)[cite: 7]. Por isso, a acurácia isolada é enganosa e o foco foi em métricas como **Recall, F1-Score, ROC-AUC e PR-AUC**.
2. **Teor Alcoólico (`alcohol`):** Forte associação positiva com a qualidade (+0.410 no target binário; +0.486 na nota contínua). Vinhos nobres apresentam teores alcoólicos mais elevados e equilibrados, frutos de uvas com maturação fenólica ideal.
3. **Acidez Volátil (`volatile acidity`):** Forte associação negativa (-0.302 no target binário; -0.409 na nota contínua). Níveis elevados de ácido acético (vinagre) degradam o aroma e o sabor.
4. **Sulfatos (`sulphates`) e Ácido Cítrico (`citric acid`):** Associações positivas relevantes (+0.213 e +0.237), agindo como antioxidantes, antimicrobianos e conferindo frescor.

---

## ⚙️ Pré-processamento & Feature Engineering

* **Limpeza:** Remoção da coluna de identificação `Id` (para evitar *data leakage*) e eliminação de duplicidades.
* **Novas Features Enológicas:**
  * `bound_sulfur_dioxide`: Dióxido de enxofre ligado (`total SO2` - `free SO2`).
  * `acidity_ratio`: Razão entre ácidos fixos desejáveis e acidez volátil indesejável.
  * `free_sulfur_ratio`: Fração de SO₂ livre no total (fração ativa contra oxidação).
* **Estratificação:** Divisão treino/teste (75/25) com `StratifiedKFold` para preservar a proporção de 13,5% de vinhos nobres em todos os splits (763 treino / 255 teste).
* **Tratamento de Desbalanceamento:** Utilização de `class_weight='balanced'` e `scale_pos_weight` nos algoritmos.

---

## 🤖 Desempenho e Seleção dos Modelos

Na etapa de **Validação Cruzada Estratificada (5-Fold)** no conjunto de treino, foram comparados três algoritmos:

| Modelo | Acurácia Média | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: |
| **XGBoost (com pesos)** 🏆 | **87,4%** | **54,5%** | **0,539** | **0,873** |
| **Regressão Logística (Balanced)** | 78,9% | 78,7% | 0,505 | 0,874 |
| **Random Forest (Balanced)** | 88,6% | 40,0% | 0,482 | 0,882 |

> **Modelo Campeão:** O **XGBoost** foi selecionado por apresentar o melhor equilíbrio operacional entre encontrar os vinhos nobres e evitar falsos alarmes, conquistando o **maior F1-Score (0,539)** no treino.

### 🎯 Calibração de Threshold e Avaliação no Teste (255 amostras não vistas)

O ponto de corte de probabilidade foi otimizado para **0,42** utilizando estritamente previsões *out-of-fold* do treino (sem vazamento para o teste):

| Cenário | Acurácia | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: |
| **Threshold Padrão (0,50)** | 89,0% | 61,8% | **0,600** | **0,915** |
| **Threshold Otimizado (0,42)** | 87,8% | 61,8% | 0,575 | **0,915** |

---

## 📊 Principais Drivers de Qualidade (Permutation Importance)

Avaliando o impacto na queda de **F1-Score** no conjunto de teste, as características físico-químicas de maior relevância preditiva foram:

1. **Sulfatos (`sulphates`):** Impacto de +0.1792
2. **Teor Alcoólico (`alcohol`):** Impacto de +0.1419
3. **Ácido Cítrico (`citric acid`):** Impacto de +0.0821
4. **Acidez Volátil (`volatile acidity`):** Impacto de +0.0726
5. **Densidade (`density`):** Impacto de +0.0653

---

## 👥 Autores do Projeto

* **David da Silva Batista**
* **Jailson da Rosa Barduino**
* **Leonardo José da Silva**
* **Raíssa Vaz Viriato**
* **Yara Maria Santos Morais**

---

## 📁 Estrutura de Pastas do Repositório

```text
wine-quality-classification/
│
├── data/              # Base de dados original (WineQT.csv)
├── notebooks/         # Notebooks com EDA, pré-processamento e modelagem
├── presentation/      # Apresentação executiva em PDF e PPTX
├── results/           # Gráficos (.png) e métricas (.csv) gerados
├── src/               # Módulos em Python auxiliar (limpeza, engenharia e treino)
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do ambiente Python
