import multifil
import multifil.aws
metas = multifil.aws.metas

freq = float(input("frequency: "))

ms_p_c = 1000 / freq
rl = 13 * ms_p_c
ts_l = 1 / 4

time_trace = metas.time(timestep_length=ts_l, run_length_in_ms=rl)

length_trace = metas.zline_workloop(mean=1250, amp=2.5, freq=freq, time=time_trace)

path_local = "./"
wl_meta, run_name = multifil.aws.metas.emit(path_local, # local dir to save run output to
                                  None, #s3 bucket to upload results to
                                  time_trace, 
                                  0.0, # poisson ratio, set to const vol here
                                 None, # intial ls, using default by passing none
                                 length_trace, 
                                 1.0, 
                                 str(freq), # comment describing run
                                 True, # whether to write out resulting file 
                                  #or just pass back to variable
                                 )
run = multifil.aws.run.manage(run_name, False)
run.run_and_save()