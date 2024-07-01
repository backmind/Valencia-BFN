# Battle of the Neighborhoods

This repository contains the project files for the IBM Data Science Professional Certificate capstone project titled **"Analyzing Socioeconomic Indicators for Relocation Recommendations in Valencia"** by Yasser Fuentes-Edfuf.

## Jump directly to the results

If you wish, you can go directly to the
- [Jupyter Notebook](https://github.com/backmind/Valencia-BFN/blob/main/notebooks/Battle%20of%20the%20Neighborhoods.ipynb)
- [PDF Report](https://github.com/backmind/Valencia-BFN/blob/main/report/Battle%20of%20the%20Neighborhoods.pdf)
- [Powerpoint Presentation](https://github.com/backmind/Valencia-BFN/blob/main/report/Presentation%20Battle%20of%20Valencia%20Neighborhoods.pdf)

## Introduction

This project aims to analyze various socioeconomic indicators in the city of Valencia, Spain, to provide relocation recommendations for new employees of a business expanding its operations in the city. The goal is to help prospective employees find suitable neighborhoods based on their socioeconomic conditions and preferences.

## Business Understanding

### Background

Valencia, a major business hub in Spain, is attractive due to its excellent infrastructure, fiscal incentives, and entrepreneurial culture. However, the cost of living varies significantly across its neighborhoods. This project seeks to leverage these variations to recommend affordable and suitable places to live for new employees.

### Problem Description

A business in Valencia is expanding and recruiting talent from outside the city. To aid new employees in settling down, an analysis of the city's neighborhoods based on various socioeconomic indicators is necessary. The insights derived will help tailor real estate recommendations to match different salary levels, thereby enhancing employee satisfaction and retention.

### Key Indicators

The analysis focuses on the following indicators:

- Population
- Average income
- Crime levels
- Amenities in the neighborhood
- Real estate and rent prices per square meter

### Target Audience

The primary audience is the management of the expanding business and their new employees. Additionally, anyone interested in living in Valencia could benefit from the insights provided.

### Success Criteria

The project is deemed successful if it can present a tiered list of Valencia's neighborhoods based on socioeconomic and business diversity, helping prospective employees make informed living choices.

## Data ETL

### Data Sources

1. **Geographical Data**: API from mapas.valencia.es
2. **Population Data**: Valencia City Council's data bank
3. **Income Data**: Spanish National Statistics Institute (INE)
4. **Real Estate Data**: Idealista website
5. **Crime Data**: Valencia Council statistical review
6. **Amenities Data**: Foursquare API

### Data Processing

1. **Geographical Data**: Converted from .gml to geojson format using `geopandas`. Calculated areas and centroids for neighborhoods and districts.
2. **Population Data**: Aggregated population data by neighborhood.
3. **Income Data**: Processed JSON data from INE to extract mean gross income per person by neighborhood.
4. **Real Estate Data**: Scraped and processed data for average rent and sale prices per neighborhood from Idealista.
5. **Crime Data**: Extracted and normalized crime data by district and then by neighborhood.
6. **Amenities Data**: Retrieved number of venues per neighborhood using Foursquare API.

## Analysis

The analysis includes visualizations and exploratory data analysis (EDA) for each indicator:

- **Geographical**: Maps showing neighborhood boundaries and centroids.
- **Population**: Density maps and statistical summaries.
- **Income**: Distribution and maps of average income per neighborhood.
- **Real Estate**: Maps and statistical summaries for rent and sale prices.
- **Crime**: Normalized crime rates visualized on maps.
- **Amenities**: Number of venues indicating economic activity levels.

## Machine Learning

A K-means clustering algorithm is used to segment neighborhoods based on the combined socioeconomic data, providing insights into distinct clusters of neighborhoods in Valencia.

## Visualizations

Interactive maps and charts are generated for each socioeconomic indicator to provide a comprehensive view of the data.

## Conclusion

The project provides valuable insights into the socioeconomic conditions of Valencia's neighborhoods, assisting new employees in finding suitable places to live and contributing to the business's employee satisfaction and retention efforts.

## Repository Structure

- `data/`: Contains static data files used in the analysis.
- `notebooks/`: Jupyter notebooks with the project code.
- `visualizations/`: Generated maps and charts.
- `report/`: Final report and additional documentation.

## How to Run

1. Clone the repository.
2. Install required packages from `requirements.txt`.
3. Run the Jupyter notebooks in the `notebooks/` directory to reproduce the analysis.

## Author

Yasser Fuentes-Edfuf

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
