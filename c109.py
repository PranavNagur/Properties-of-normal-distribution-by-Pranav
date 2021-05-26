import pandas as pd
import csv
import statistics


df=pd.read_csv('c109.csv')
height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()


height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print('Mean,Median and Mode of height is {},{},{}'.format(height_mean, height_median, height_mode))
print('Mean,Median and Mode of weight is {},{},{}'.format(weight_mean, weight_median, weight_mode))

height_std=statistics.stdev(height_list)
weight_std=statistics.stdev(weight_list)

height_first_std_start,height_first_std_end = height_mean-height_std,height_mean+height_std
height_second_std_start,height_second_std_end = height_mean-(2*height_std),height_mean+(2*height_std)
height_third_std_start,height_third_std_end = height_mean-(3*height_std),height_mean+(3*height_std)

weight_first_std_start,weight_first_std_end = weight_mean-weight_std,weight_mean+weight_std
weight_second_std_start,weight_second_std_end = weight_mean-(2*weight_std),weight_mean+(2*weight_std)
weight_third_std_start,weight_third_std_end = weight_mean-(3*weight_std),weight_mean+(3*weight_std)



height_list_of_data_within_onestd=[result for result in height_list if result>height_first_std_start and result<height_first_std_end]
height_list_of_data_within_twostd=[result for result in height_list if result>height_second_std_start and result<height_second_std_end]
height_list_of_data_within_threestd=[result for result in height_list if result>height_third_std_start and result<height_third_std_end]

weight_list_of_data_within_onestd=[result for result in weight_list if result>weight_first_std_start and result<weight_first_std_end]
weight_list_of_data_within_twostd=[result for result in weight_list if result>weight_second_std_start and result<weight_second_std_end]
weight_list_of_data_within_threestd=[result for result in weight_list if result>weight_third_std_start and result<weight_third_std_end]


print('{}% of data for height lies within one stdev'.format(len(height_list_of_data_within_onestd)*100.0/len(height_list)))
print('{}% of data for height lies within two stdev'.format(len(height_list_of_data_within_twostd)*100.0/len(height_list)))
print('{}% of data for height lies within three stdev'.format(len(height_list_of_data_within_threestd)*100.0/len(height_list)))

print('{}% of data for weight lies within one stdev'.format(len(weight_list_of_data_within_onestd)*100.0/len(weight_list)))
print('{}% of data for weight lies within two stdev'.format(len(weight_list_of_data_within_twostd)*100.0/len(weight_list)))
print('{}% of data for weight lies within three stdev'.format(len(weight_list_of_data_within_threestd)*100.0/len(weight_list)))