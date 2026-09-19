# 🧠 Machine Learning: Portfólio de Projetos e Algoritmos

Bem-vindo ao repositório **machine-learning-projetos**! Este espaço reúne uma coleção de projetos práticos e estudos de caso em Aprendizado de Máquina, cobrindo desde algoritmos fundamentais até técnicas avançadas de Engenharia de IA para problemas do mundo real.

---

## 📂 Projetos Incluídos no Repositório

### 1. 🔄 Previsão de Cancelamento de Assinatura (Churn)
* **Algoritmo:** Árvore de Decisão (`DecisionTreeClassifier`)
* **Descrição:** Modelo preditivo para identificar clientes de um serviço de streaming com alta probabilidade de cancelar a assinatura.
* **Variáveis:** Dias de atividade, chamados ao suporte e média de músicas ouvidas por dia.

### 2. 🏦 Concessão Preditiva de Empréstimo Bancário
* **Algoritmo:** Árvore de Decisão (`DecisionTreeClassifier`)
* **Descrição:** Sistema de análise de risco de crédito que classifica solicitações de empréstimo em aprovadas ou recusadas.
* **Variáveis:** Renda mensal, score de crédito e restrição no nome (nome sujo).

### 3. 🏭 Manutenção Preditiva na Indústria 4.0
* **Algoritmo:** Árvore de Decisão (`DecisionTreeClassifier`)
* **Descrição:** Diagnóstico em tempo real de máquinas industriais para prever falhas mecânicas antes que ocorram paradas na produção.
* **Variáveis:** Telemetria de temperatura, nível de vibração, pressão e horas de uso contínuo.
* **Avaliação:** Uso do `classification_report` para métricas de falha iminente.

### 4. 🚨 Detecção de Fraudes Financeiras (Dados Desbalanceados)
* **Algoritmo:** Floresta Aleatória (`RandomForestClassifier`)
* **Descrição:** Modelo avançado para identificação de transações fraudulentas em cenários reais com alto desbalanceamento de classes (~5% de fraudes).
* **Técnicas Aplicadas:** 
  * Estratificação de dados (`stratify=y`).
  * Penalização por pesos de classe (`class_weight='balanced'`).
  * Avaliação por **Matriz de Confusão**, **Recall** e **Precision**.
  * Análise de importância de atributos (*Feature Importance*).

---

## 🛠️ Tecnologias e Bibliotecas

* **Linguagem:** Python 3.x
* **Manipulação de Dados:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn`
* **Visualização:** `matplotlib`

---

## 📊 Métricas de Avaliação Trabalhadas

Para garantir modelos robustos e alinhados a problemas reais de negócio, o repositório aborda:
* **Acurácia:** Medição geral do modelo.
* **Matriz de Confusão:** Mapeamento de Verdadeiros/Falsos Positivos e Negativos.
* **Precision & Recall:** Foco na redução de alarmes falsos e na captura de eventos críticos (fraudes e falhas).
* **Feature Importance:** Identificação das variáveis com maior impacto na tomada de decisão.

---

## 🚀 Como Executar os Projetos

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/DevAlexandreDias/machine-learning-projetos.git](https://github.com/DevAlexandreDias/machine-learning-projetos.git)
   cd machine-learning-projetos
