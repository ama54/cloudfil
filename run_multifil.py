import multifil
import multifil.aws
metas = multifil.aws.metas

ts_p_ms = int(input("timesteps per millisecond: "))
rl = int(input("run length: "))
freq = float(input("frequency: "))
ts_l = 1 / ts_p_ms

time_trace = metas.time(timestep_length=ts_l, run_length_in_ms=rl)

length_trace = metas.zline_workloop(mean=1200, amp=2.5, freq=freq, time=time_trace)

path_local = "./"
wl_meta, run_name = multifil.aws.metas.emit(path_local, # local dir to save run output to
                                  None, #s3 bucket to upload results to
                                  time_trace, 
                                  0.5, # poisson ratio, set to const vol here
                                 None, # intial ls, using default by passing none
                                 length_trace, 
                                 1.0, 
                                 "an example run", # comment describing run
                                 True, # whether to write out resulting file 
                                  #or just pass back to variable
                                 )
run = multifil.aws.run.manage(run_name, False)
run.run_and_save()