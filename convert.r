# Set working directory
setwd("/Users/winniche/Documents/cs448b")

# Set CRAN mirror for package installation
options(repos = c(CRAN = "https://cran.rstudio.com/"))

# Install ipumsr if needed
if (!require("ipumsr")) install.packages("ipumsr")

# Load package
library(ipumsr)

# Read the data
ddi <- read_ipums_ddi("atus_00004.xml")
data <- read_ipums_micro(ddi)

# Save as CSV
write.csv(data, "atus_data2.csv", row.names = FALSE)

print("Done! CSV file created.")