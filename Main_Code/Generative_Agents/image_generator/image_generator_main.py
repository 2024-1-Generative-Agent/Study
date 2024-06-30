import openai
import pandas as pd
import os

#==============================================#
# 
#
#
#==============================================#

def generate_image(prompt, x, y, csv_file='image_coordinates.csv'):
    
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']

    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=['x', 'y', 'prompt', 'url'])
    else:
        df = pd.read_csv(csv_file)
    
    #-------- Replace old value ------------------#
    index = df[(df['x'] == x) & (df['y'] == y)].index
    if len(index) > 0:
        df.loc[index, 'prompt'] = prompt
        df.loc[index, 'url'] = image_url
    else:
        df = df.append({'x': x, 'y': y, 'prompt': prompt, 'url': image_url}, ignore_index=True)
    df.to_csv(csv_file, index=False)
    #--------------------------------------------#

    return image_url


if __name__=="__main__":
    prompt = "A beautiful landscape with mountains and a river"
    x, y = 10, 20
    image_url = generate_image(prompt, x, y)
    print(f"Generated image URL: {image_url}")
