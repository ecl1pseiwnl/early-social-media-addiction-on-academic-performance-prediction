import pandas as pd


# Load raw dataset file
try:
    dframe = pd.read_csv("social-media-impact-dataset.csv")

    # Define target columns
    target_column = [
                    "Age", "Gender", "Academic_Level", 
                     "Primary_Platform", "Daily_Usage_Hours", "Weekend_Extra_Hours",
                     "Device_Type", "Sleep_Duration_Hours", "Sleep_Quality_Score",
                     "Late_Night_Usage", "Social_Comparison_Frequency", "Perceived_Stress_Score",
                     "Mental_Health_Index", "Academic_Performance_GPA", "Overall_Impact"
                ]
    
    existing_columns = [col for col in target_column if col in dframe]
    dframe_filtered = dframe[existing_columns]
    
    # Save as a new csv file
    filename_output = "filtered-dataset.csv"
    dframe_filtered.to_csv(filename_output,index = False)
    
    print(f"Sucessfully filtered and created {filename_output} with columns")
    print(existing_columns)
    print(f"\nShape: {dframe_filtered.shape}")    
    
except Exception as e:
    print(f"Error: {e}")