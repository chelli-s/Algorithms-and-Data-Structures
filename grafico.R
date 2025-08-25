# Installare i pacchetti necessari se non sono già installati
install.packages("ggplot2")

# Caricare i pacchetti
library(ggplot2)

# Nome del file CSV
file_name <- "dati.csv"

# Lettura dei dati dal file CSV
df <- read.csv(file_name)

# Creazione del grafico
grafico <- ggplot(df, aes(x = lunghezza_n)) +
  geom_line(aes(y = quickSelect, color = "quickSelect")) +
  geom_line(aes(y = heapSelect, color = "heapSelect")) +
  geom_line(aes(y = medianOfMedians, color = "medianOfMedians")) +
  labs(title = "Tempi di esecuzione in funzione di lunghezza n",
       x = "lunghezza n",
       y = "Tempo (secondi)") +
  scale_color_manual(values = c("quickSelect" = "blue", "heapSelect" = "red", "medianOfMedians" = "green"),
                     name = "Algoritmi") +
  theme_minimal()

# Visualizzazione del grafico
print(grafico)

# Salva il grafico come file PNG
ggsave("performance_plot.png", plot = grafico)

