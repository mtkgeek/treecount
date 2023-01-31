
# Install necessary packages and load them

if(!"ForestTools" %in% installed.packages()){install.packages("ForestTools")}
if(!"raster" %in% installed.packages()){install.packages("raster")}
if(!"rgdal" %in% installed.packages()){install.packages("rgdal")}


# import 'ForestTools' and 'raster' libraries
library(ForestTools)
library(raster)
library(rgdal)


retrieve_CHM <- function() {
   
    # Load sample canopy height model
    chm <- raster('data/challenge2_WUR_S4G/CHM.tif')
    
    # Remove plot margins (optional)
    par(mar = rep(0.5, 4))
    
    return(chm)
  }



detect_treetops <- function(chm_var) {
  # Detecting treetops
  # Dominant treetops can be detected using vwf
  lin <-
    function(x) {
      x * 0.05 + 0.6
    } # function that defines the dynamic window size
  
  # Set a minimum height of 2 m using the minHeight argument.
  # Any cell with a lower value will not be tagged as a treetop.
  # This will prevent shrubs and small bushes from being tagged as trees
  ttops <- vwf(CHM = chm_var,
               winFun = lin,
               minHeight = 2)
  
  # Get number of trees
  total_no_trees <- sp_summarise(ttops)
  
  print(paste("total number of tree tops:", total_no_trees))
  # Get the average, max and even min treetop height (you can confirm if this is correct by comparing values with a visual inspection of the chm on qgis for e.g)
  max_height = max(ttops$height)
  min_height = min(ttops$height)
  average_height = mean(ttops$height)
  print(paste("maximum tree height is:", max_height))
  print(paste("minimum tree height is:", min_height))
  print(paste("average tree height is:", average_height))
  return(ttops)
}
# Outlining tree crowns #

create_crownMap <- function(chm, ttops) {
  # Create crown map
  crowns <-
    mcws(
      treetops = ttops,
      CHM = chm,
      minHeight = 1.5,
      verbose = FALSE
    )
  
  # estimate the number of tree species
  colors <- sample(rainbow(50), length(unique(crowns[])), replace = TRUE)
  total_number_of_species <- length(unique(colors))
  
  print(paste(
    "estimate of total number of species:",
    total_number_of_species
  ))
  
  # # Create polygon crown map
  crownsPoly <-
    mcws(
      treetops = ttops,
      CHM = chm,
      format = "polygons",
      minHeight = 1.5,
      verbose = FALSE
    )
  writeOGR(
    crownsPoly,
    dsn = 'output/crownPoly.GeoJSON',
    layer = "CrownPoly",
    overwrite_layer = TRUE, driver = "GeoJSON"
  )
  dev.off()
  return(list(crowns, crownsPoly, total_number_of_species))
}

RGB_image <-
  function(path = "data/challenge2_WUR_S4G/Multispectral.tif") {
    # Load the image data into R
    image <- stack(path)
    
    # Get the names of the bands in the image data
    bands <- names(image)
    
    # Select the red, green, and blue bands
    rgb <-
      stack(image[[bands[1]]], image[[bands[2]]], image[[bands[3]]])
    return(rgb)
  }


setup_function <- function() {
  # Create input folder if not yet existent
if (!dir.exists('data/challenge2_WUR_S4G')) {
  dir.create('data/challenge2_WUR_S4G/')
}

# Create output folder if not yet existent
if (!dir.exists('output')) {
  dir.create('output')
}
}

main_function <- function() {

chm <- retrieve_CHM()

ttops <- detect_treetops(chm)

x <- create_crownMap(chm, ttops)
crown_rast <- x[[1]]
crown_poly <- x[[2]]
estimate_tree_species <- x[[3]]

rgb <- RGB_image()

#####Making some plots for visualization#####

# Create and save a chm plot
png(filename = "data/original_CHM.png", width = 800, height = 500)
# Plot CHM (extra optional arguments remove labels and tick marks from the plot)
plot(chm, xlab = "", ylab = "", xaxt='n', yaxt = 'n')

# close device
dev.off()

# We can now plot these treetops on top of the CHM.

# Create and save tree tops plot
png(filename = "output/ttops_CHM.png", width = 800, height = 500)

# Plot CHM
plot(chm, xlab = "", ylab = "", xaxt='n', yaxt = 'n')

# Add dominant treetops to the plot
plot(ttops, col = "blue", pch = 20, cex = 0.5, add = TRUE)

# close device
dev.off()
# Create and save tree tops plot
png(filename = "output/ttops_CHM.png", width = 800, height = 500)

# Plot CHM
plot(chm, xlab = "", ylab = "", xaxt='n', yaxt = 'n')

# Add dominant treetops to the plot
plot(ttops, col = "blue", pch = 20, cex = 0.5, add = TRUE)

# close device
dev.off()

# Create and save tree crowns plot
png(filename = "output/crown_CHM.png", width = 800, height = 500)

# Plot crowns
plot(crown_rast, col = sample(rainbow(50), length(unique(crown_rast[])), replace = TRUE), legend = FALSE, xlab = "", ylab = "", xaxt='n', yaxt = 'n')

# close device
dev.off()

# Create and save tree crowns plot
png(filename = "output/crownsPoly.png", width = 800, height = 500)

# Plot the RGB image
plotRGB(rgb, stretch = "lin")

# Add crown outlines to the plot
plot(crown_poly, border = "red", lwd = 0.5, add = TRUE)

dev.off()
}
