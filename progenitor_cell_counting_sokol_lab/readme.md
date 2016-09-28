# Counting the progenitor cell
______________________
## Description  
The goal of this project is to develop a workflow to automate the process from image processing to progenitor cell counting and basic statistics. We are comparing the wildtype *Drosophila* with different *Drosophila* mutants.     

The traditional appraoch (manual counting or imageJ counting) is both slow and inaccurate. Thus, I tested few filtering strategies and settled with LoG (**Laplacian of Gaussian**) and then implemented using a module in scikit learn. I also implemented multi-threading to decrease the runtime to accelerate the analysis duration.

The project utilizes multiple modules including: numpy, scipy, scikit learn, pandas, matplotlib, etc..

Overall, this workflow recgonize/counting cells with very high precision.
We believe that this workflow increase the efficiency significantly for Sokol Lab.

Shengyao
