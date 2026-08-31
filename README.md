# 🍷 Predição da Qualidade de Vinhos

Este repositório contém a solução do Tech Challenge - Fase 2 da pós-graduação.  
O objetivo do projeto é desenvolver um modelo de classificação capaz de prever a qualidade de um vinho com base em suas características físico-químicas. Para simplificar o problema, a variável de qualidade deverá ser transformada em uma **classificação binária** capaz de prever se um vinho é de **alta qualidade (nota ≥ 7)** ou **baixa/média qualidade (nota < 7)**.

---

## 📺 Entregáveis Executivos

O conteúdo sintetiza as dores identificadas, os dados analisados, os principais insights e as recomendações estratégicas relacionadas à qualidade dos vinhos.
Os resultados foram organizados em gráficos e tabelas comparativas, com foco em **storytelling de negócios**.

* ▶️ **Vídeo da Apresentação Executiva (YouTube):** [Clique aqui para assistir ao vídeo](https://www.youtube.com/)
* 📊 **Apresentação em Slides (PDF):** [`presentation/Apresentacao_Executiva_Vinhos.pptx`](./presentation/)
* 📓 **Jupyter Notebook Completo:** [`notebooks/TechChallengeVinho_Otimizado.ipynb`](./notebooks/)

---

## 🔍 Principais Insights da Análise Exploratória (EDA)

A base final conta com **1.018 amostras únicas** após o tratamento de 125 duplicidades.

1. **Desbalanceamento Severo:** Vinhos de alta qualidade representam apenas **~13,5%** da base (137 amostras), enquanto vinhos comuns representam **86,5%** (881 amostras). Por isso, a acurácia isolada é enganosa e o foco foi em métricas como **Recall, F1-Score e ROC-AUC**.
2. **Teor Alcoólico (`alcohol`):** Forte correlação positiva (+0.48 com a qualidade). Vinhos nobres apresentam teores alcoólicos mais elevados e equilibrados, frutos de uvas com maturação fenólica ideal.
3. **Acidez Volátil (`volatile acidity`):** Forte correlação negativa (-0.41 com a qualidade). Níveis elevados de ácido acético (vinagre) degradam o aroma e sabor.
4. **Sulfatos (`sulphates`) e Ácido Cítrico (`citric acid`):** Correlações positivas relevantes (+0.25 e +0.24). Agem conferindo frescor e proteção antimicrobiana/antioxidante.

---

## ⚙️ Pré-processamento & Feature Engineering

* **Limpeza:** Remoção da coluna de índice `Id` (para evitar *data leakage*) e eliminação de duplicidades.
* **Novas Features Enológicas:**
  * `bound_sulfur_dioxide`: Dióxido de enxofre ligado (`total SO2` - `free SO2`).
  * `acidity_ratio`: Razão entre ácidos fixos desejáveis e acidez volátil indesejável.
  * `free_sulfur_ratio`: Fração de SO2 livre no total (fração ativa contra oxidação).
* **Estratificação:** Divisão treino/teste (75/25) com `StratifiedKFold` para preservar a proporção de 13,5% de vinhos nobres em todos os splits.
* **Tratamento de Desbalanceamento:** Utilização de `class_weight='balanced'` e `scale_pos_weight` nos algoritmos.

---

## 🤖 Desempenho dos Modelos

Foram comparados três algoritmos de classificação:

| Modelo | Acurácia | Precisão | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Forest (Balanced)** 🏆 | **91,0%** | **78,9%** | **44,1%** | **0,57** | **0,92** |
| **XGBoost (Weighted)** | 87,5% | 56,0% | 50,0% | 0,53 | 0,82 |
| **Logistic Regression (Balanced)** | 79,6% | 37,1% | 76,5% | 0,50 | 0,89 |

> **Modelo Campeão:** O **Random Forest** alcançou **0,92 de ROC-AUC** e a maior precisão na classe positiva (78,9%), minimizando drasticamente o risco de falsos positivos (rotular vinho comum como nobre).

---

## 👥 Autores do Projeto

- David da Silva Batista
- Jailson da Rosa Barduino
- Leonardo José da Silva
- Raíssa Vaz Viriato
- Yara Maria Santos Morais

---

## 📁 Estrutura de Pastas do Repositório
```
wine-quality-classification/
│
├── data/              # Base de dados original (WineQT.csv)
├── notebooks/         # Notebooks com EDA, pré-processamento e modelagem
├── src/               # Módulos em Python auxiliar (limpeza, engenharia e treino)
├── results/           # Gráficos (.png) e métricas (.csv) gerados
├── presentation/      # Apresentação executiva em PDF e PPTX
├── requirements.txt   # Dependências do ambiente Python
└── README.md          # Documentação do projeto
```


