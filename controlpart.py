from moviefiter import moviedata
import pandas as pd
def mainpart():
    user_1=moviedata()
    user_ing=input("genres:")
    # for multiple genres use , for seperation between each keywords.
    user_inc=input("casts: ")
    #user_inr=input("rates: ")
    user_date=input("date: ")
    genresls=user_ing.lstrip().rstrip().split(",")
    castls=user_inc.lstrip().rstrip().split(",")
    datels=int(user_date.lstrip().rstrip()[0:4])
    wanted_df=moviedata.search(user_1.movies_df,Only=False,genres=genresls,cast=castls)
    secondpart=moviedata.search(user_1.movies_df,Only=False,genres=genresls)
    final_one=pd.concat([wanted_df,secondpart],axis=0)
    final_one.drop_duplicates(subset=['id'],keep='first',inplace=True)
    moviedata.forsort(wanted_df,datels)
    if wanted_df.shape[0]>100:
        return wanted_df.head(100)
    else:
        return wanted_df
    
mainpart()

