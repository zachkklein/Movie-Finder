from moviefiter import moviedata
import pandas as pd
import threading as td
import datetime
import time
from concurrent.futures import ProcessPoolExecutor


"""def mainpart0_1(): #slower version
   
    user_ing=input("genres:")  #input by terminal
    #user_ing="animation,horror,funny,lol" #input genres
    # for multiple genres use "," to seperate each keywords.
    user_inc=input("casts: ") #by terminal
    #user_inc="tom hanks"       #input actors
    user_date=input("date: ")
    #user_date="2011"           #input datetime
    if len(user_ing.lstrip().rstrip())>0:
        genresls=user_ing.lstrip().rstrip().split(",")
    else:
        genresls=[]
    #print(genresls)
    if len(user_inc.lstrip().rstrip())>0:
        castls=user_inc.lstrip().rstrip().split(",")
    else:
        castls=[]
    #print(castls)
    if len(user_date.lstrip().rstrip())>=4:
        datels=user_date.lstrip().rstrip()[0:4]
    else:
        datels=str(datetime.datetime.today().year)
    #print(datels)
    #newp_global_ones=[]
    No_cast=False
    No_genre=False

    if len(genresls)>0:
        args_gc={"genres":genresls}
        td_gc=td.Thread(
            target=user_1.search,
            args=(user_1.movies_df,),kwargs={"Only":False,**args_gc} #simply nope 
            )
        #print("UYESE UITW ORKDS")
        
        td_gc.start()
        if len(castls)>0:
            wanted_df=user_1.search(user_1.movies_df,Only=False,upload=False,genres=genresls,cast=castls)
        else:
            wanted_df=pd.DataFrame()
            No_cast=True
        td_gc.join()
    else:
        No_genre=True

    secondpart=user_1.newp_global_ones
    #print(secondpart)
    if No_cast and No_genre:
        final_one=user_1.movies_df.head(10)
    else:
        
        final_one=pd.concat([wanted_df,secondpart],axis=0)

    final_one.drop_duplicates(subset=['id'],keep='first',inplace=True)
    final_one=moviedata.forsort(final_one,datels)


    if final_one.shape[0]>10:
        return final_one.head(10)
    else:
        return final_one
"""

def mainpart(user_ing,user_inc,user_date):
   
    
    if len(user_ing.lstrip().rstrip())>0:
        genresls=user_ing.lstrip().rstrip().split(",")
    else:
        genresls=[]
    #print(genresls)
    if len(user_inc.lstrip().rstrip())>0:
        castls=user_inc.lstrip().rstrip().split(",")
    else:
        castls=[]
    #print(castls)
    if len(user_date.lstrip().rstrip())>=4:
        datels=user_date.lstrip().rstrip()[0:4]
    else:
        datels=""
    #print(datels)
    #newp_global_ones=[]
    No_cast=False
    No_genre=False

    if len(genresls)>0:
        #args_gc={"genres":genresls}
        #td_gc=td.Thread(
        #    target=user_1.search,
        #    args=(user_1.movies_df,),kwargs={"Only":False,**args_gc} #simply nope 
        #    )
        pool1=ProcessPoolExecutor(max_workers=2)
        add_kwargs_gu={"genres":genresls}
        gu=pool1.submit(user_1.search,user_1.movies_df,Only=False,**add_kwargs_gu)
                #secondpart=gu.result()
        #print("UYESE UITW ORKDS")
        
        #td_gc.start()
        if len(castls)>0:
            
            #wanted_df=user_1.search(user_1.movies_df,Only=False,upload=False,genres=genresls,cast=castls)
            #pool=ProcessPoolExecutor()
            add_kwargs={"genres":genresls,"cast":castls}
            cu=pool1.submit(user_1.search,user_1.movies_df,Only=False,**add_kwargs)
                #wanted_df=cu.result()
        else:
            #wanted_df=pd.DataFrame(columns=user_1.movies_df.columns)
            No_cast=True
        #td_gc.join()
    else:
        No_genre=True
    
    #pool.shutdown(wait=True,cancel_futures=False)
    pool1.shutdown(wait=True,cancel_futures=False)
    if not No_cast:
        #print(user_1.newp_global_ones)
        wanted_df=cu.result()
    else:
        wanted_df=pd.DataFrame(columns=user_1.movies_df.columns)
    if not No_genre:
        #print(user_1.newp_global_ones)
        secondpart=gu.result()
    else:
        secondpart=user_1.movies_df
    #print(secondpart)
    if No_cast and No_genre:
        final_one=user_1.movies_df.head(10)
    else:
        final_one=pd.DataFrame(columns=user_1.movies_df.columns)
        if not No_cast:
            final_one=pd.merge(wanted_df,secondpart,how="inner") #求补集,wanted是大，secondpart是细
        final_one=pd.concat([final_one,secondpart,wanted_df],axis=0).drop_duplicates(subset=["id"],keep="first")
    if not user_date=="":
        final_one=moviedata.forsort(final_one,datels)


    if final_one.shape[0]>10:
        return final_one.head(10)
    else:
        return final_one


def df_tolist(df:pd.DataFrame):
    final_output=[]
    for row in range(1):
        id_ofmovie=df["id"].iloc[row] #HERE to put id eg.862 all in str
        output=user_1.alles_inner_extract(movie_ids=[id_ofmovie],rEALLYONLY=True) #using id of the movie to extract data
        final_output.append(output)
    return final_output
        
    #OUTPUT FORMAT:
    #!!! if shown nan means this movie does not has this section.Just skip   
    #get every row by final_output[row]
    #get each elements in each row by following: 
    #final_output[row][position]
    #data type: str
    #position: 0:movie_id for input upon  
    #position: 1 overview, can be add to shown on the page  
    #position: 2 tagline, a line of words can be also add to page
    #position: 3 a list of main actors.
    #position: 4 a list of genres of this movie
    #position: 5 a list of maker of this movie
    #position: 6 a list of the of country of this movie  format: "XX_[Country]"
    #position: 7 the year it released

def showtime(x,g,c,d):
    start=time.time()
    temp=x(g,c,d)
    print(f"used time: {time.time()-start}")
    return temp

def go_input():
    user_ing=input("genres:")  #input by terminal
    #user_ing="animation" #input genres
    # for multiple genres use "," to seperate each keywords.
    user_inc=input("casts: ") #by terminal
    #user_inc=""       #input actors
    user_date=input("date: ")
    return [user_ing,user_inc,user_date]
if __name__ == "__main__": #press ctrl+c to stop!
    try:
        startpole=ProcessPoolExecutor() 
        user_1_fu=startpole.submit(moviedata)
        
        #_gcd=user_input_fu.result()
        
        
        
        while True:
            
            _gcd=go_input()
            #print(startpole._queue_count)
            if startpole._queue_count>0:
                user_1=user_1_fu.result()
                startpole.shutdown(wait=True) 
            
            #user_date="2011"           #input datetime
            show_me=showtime(mainpart,_gcd[0],_gcd[1],_gcd[2])
            print(show_me["original_title"])
    except:
            exit("End")   