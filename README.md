# vison

This is a python script that can be used to analyse ArmNN ExecuteNetwork profiler output

The output of the profiler can be generated when running a model with the -e option and should be saved into a file.

Then the vison script can be used to visualize how much time each workload takes and to see a breakdown of how much time each kernel takes over the total execution time.

Dependencies:
This script requires matplotlib and numpy to draw the charts.

Install this dependencie: pip3 install matplotlib


See below an example of running the script and the type of information which generates.

```
morg@stoic-box:~/self/vison$ python3 vison.py -j ./test.prof
Working Memory Allocation_#5
CopyMemGeneric_Execute_#6
ClConvolution2dWorkload_Execute_#8
	      600.648 us 			  im2col3x3_nhwc 
	      202.434 us 			  gemmlowp_matrix_a_reduction 
	      6158.54 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#9
	     3352.214 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#10
	      161.628 us 			  gemmlowp_matrix_a_reduction 
	    12732.747 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#11
	      117.506 us 			  gemmlowp_matrix_a_reduction 
	    15952.707 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#12
	     2609.368 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#13
	      130.564 us 			  gemmlowp_matrix_a_reduction 
	    11128.503 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#14
	       40.083 us 			  gemmlowp_matrix_a_reduction 
	     5703.373 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#15
	     3763.933 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#16
	      183.577 us 			  gemmlowp_matrix_a_reduction 
	    16405.417 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#17
	      179.066 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#18
	       41.021 us 			  gemmlowp_matrix_a_reduction 
	     6145.461 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#19
	      976.364 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#20
	       49.584 us 			  gemmlowp_matrix_a_reduction 
	      6198.87 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#21
	       13.094 us 			  gemmlowp_matrix_a_reduction 
	     9387.454 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#22
	     1261.019 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#23
	       66.741 us 			  gemmlowp_matrix_a_reduction 
	     8186.208 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#24
	       48.937 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#25
	       12.641 us 			  gemmlowp_matrix_a_reduction 
	     9632.211 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#26
	     1277.752 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#27
	       65.875 us 			  gemmlowp_matrix_a_reduction 
	      8210.08 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#28
	       46.324 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#29
	       12.741 us 			  gemmlowp_matrix_a_reduction 
	     9223.792 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#30
	      316.602 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#31
	       15.238 us 			  gemmlowp_matrix_a_reduction 
	     4845.575 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#32
	        7.742 us 			  gemmlowp_matrix_a_reduction 
	    11658.627 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#33
	      601.217 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#34
	       27.479 us 			  gemmlowp_matrix_a_reduction 
	    10596.085 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#35
	       26.334 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#36
	        7.895 us 			  gemmlowp_matrix_a_reduction 
	    11039.374 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#37
	      598.953 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#38
	       26.858 us 			  gemmlowp_matrix_a_reduction 
	     9545.167 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#39
	       27.862 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#40
	        7.788 us 			  gemmlowp_matrix_a_reduction 
	    11877.169 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#41
	      639.414 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#42
	       26.598 us 			  gemmlowp_matrix_a_reduction 
	     9495.625 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#43
	       27.162 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#44
	        7.706 us 			  gemmlowp_matrix_a_reduction 
	    11103.918 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#45
	      608.503 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#46
	       26.945 us 			  gemmlowp_matrix_a_reduction 
	    15006.164 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#47
	        9.533 us 			  gemmlowp_matrix_a_reduction 
	    23211.904 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#48
	      972.197 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#49
	       35.586 us 			  gemmlowp_matrix_a_reduction 
	    26118.834 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#50
	       37.937 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#51
	        9.965 us 			  gemmlowp_matrix_a_reduction 
	    23477.415 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#52
	      948.107 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#53
	       38.013 us 			  gemmlowp_matrix_a_reduction 
	     25349.29 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#54
	       42.526 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#55
	        6.724 us 			  gemmlowp_matrix_a_reduction 
	    22916.924 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#56
	      232.711 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#57
	       18.557 us 			  gemmlowp_matrix_a_reduction 
	    10678.373 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#58
	       10.679 us 			  gemmlowp_matrix_a_reduction 
	    18265.458 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#59
	      343.712 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#60
	       29.566 us 			  gemmlowp_matrix_a_reduction 
	    15710.751 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#61
	       19.998 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#62
	       10.376 us 			  gemmlowp_matrix_a_reduction 
	    17466.708 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#63
	      355.684 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#64
	       29.222 us 			  gemmlowp_matrix_a_reduction 
	    14726.251 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClAdditionWorkload_Execute_#65
	       19.708 us 			  elementwise_operation_ADD_quantized 
ClConvolution2dWorkload_Execute_#66
	       10.621 us 			  gemmlowp_matrix_a_reduction 
	    16682.002 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClDepthwiseConvolutionWorkload_Execute_#67
	      356.828 us 			  dwc_MxN_native_quantized8_nhwc 
ClConvolution2dWorkload_Execute_#68
	       28.548 us 			  gemmlowp_matrix_a_reduction 
	    30090.542 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClConvolution2dWorkload_Execute_#69
	       12.781 us 			  gemmlowp_matrix_a_reduction 
	    59477.167 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClPooling2dWorkload_Execute_#70
	       28.107 us 			  pooling_layer_MxN_quantized_nhwc 
ClConvolution2dWorkload_Execute_#71
	       34.039 us 			  gemmlowp_matrix_a_reduction 
	       453.07 us 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
ClReshapeWorkload_Execute_#72
	       14.828 us 			  reshape_layer 
CopyMemGeneric_Execute_#73



Inference time:  557918.542 us
Total kernel time  546727.7189999997 us

Total time per kernel				Percentage of total time		Kernel name
	 14.8280              us 		% 0.00002712 			  reshape_layer 
	 28.1070              us 		% 0.00005141 			  pooling_layer_MxN_quantized_nhwc 
	 475.8540             us 		% 0.00087037 			  elementwise_operation_ADD_quantized 
	 600.6480             us 		% 0.00109862 			  im2col3x3_nhwc 
	 1535.9480            us 		% 0.00280935 			  gemmlowp_matrix_a_reduction 
	 19214.5780           us 		% 0.03514469 			  dwc_MxN_native_quantized8_nhwc 
	 524857.7560          us 		% 0.95999844 			  gemmlowp_mm_reshaped_only_rhs_t_fused_output_stage_fixedpoint 
```

For more information about ArmNN and ExecuteNetwork visit: https://github.com/ARM-software/armnn/tree/branches/armnn_21_02/tests/ExecuteNetwork

Plans for the future:
* Add an option output charts with a summary of how much of the total time each layer takes.
* Add an option to compare two profiler files.
