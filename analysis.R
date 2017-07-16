getwd()
# Not loading more than 4123 entries
data <- read.csv("data\\data.csv", sep=",")
nrow(data)
head(data)


library(dplyr)
library(tidytext)
library(ggplot2)
library(gutenbergr)
library(scales)
library(tidyr)
library(tm)

data("stop_words")
title <- data$title
text_df <- data_frame(text=title, line=1:4123)
text_df

# some preprocessing, tolower, remove punctuations, stemming
documents <- Corpus(VectorSource(text_df$text))
documents
documents <- tm_map(documents, content_transformer(tolower))
documents <- tm_map(documents, removePunctuation)
documents <- tm_map(documents, removeWords, stopwords("english"))
documents <- tm_map(documents, stemDocument)
documents

# Create a dataframe
df <- data.frame(text = sapply(documents, as.character), stringsAsFactors = FALSE)
df$text

# unigram
tidy_desc <- df %>% unnest_tokens(word, text)
tidy_desc
tidy_desc %>% count(word, sort = TRUE)


# plot word on frequency alert name
tidy_desc  %>%
  count(word, sort = TRUE) %>%
  filter(n > 80) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

# --------------------------------------------------------------
# topic modelling
# --------------------------------------------------------------
library(topicmodels)
text_df

# some preprocessing, tolower, remove punctuations, stemming
documents <- Corpus(VectorSource(text_df$text))
documents
documents <- tm_map(documents, content_transformer(tolower))
documents <- tm_map(documents, removePunctuation)
documents <- tm_map(documents, removeWords, stopwords("english"))
documents <- tm_map(documents, stemDocument)
documents

dtm <- DocumentTermMatrix(documents, control = list(tokenize=scan_tokenizer))
dtm
colnames(dtm)
rowTotals <- apply(dtm , 1, sum)
#Find the sum of words in each Document
dtm   <- dtm[rowTotals> 0, ]

ap_lda <- LDA(dtm, k = 10, control = list(seed = 1234, verbose=1))
#ap_lda

ap_topics <- tidy(ap_lda, matrix = "beta")
#ap_topics


ap_top_terms <- ap_topics %>%
  group_by(topic) %>%
  top_n(10, beta) %>%
  ungroup() %>%
  arrange(topic, -beta)

ap_top_terms %>%
  mutate(term = reorder(term, beta)) %>%
  ggplot(aes(term, beta, fill = factor(topic))) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~ topic, scales = "free") +
  coord_flip()
