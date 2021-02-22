# R package list
dir.create(".R")
dir.create(".R/library")
.libPaths(".R/library")
install.packages(c(
    "base64enc", 
    "digest", 
    "evaluate", 
    "glue", 
    "highr", 
    "htmltools", 
    "jsonlite", 
    "knitr", 
    "magrittr", 
    "markdown", 
    "mime", 
    "rlang", 
    "rmarkdown", 
    "stringi", 
    "stringr", 
    "tinytex", 
    "xfun"), lib=".R/library")