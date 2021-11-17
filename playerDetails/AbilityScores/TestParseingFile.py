import json


if __name__== "__main__":
        f = open('characters.json')

        data = json.load(f)

        for i in data['characters']:
            print(i)
            for z in data['characters'][i]:
                for j in data['characters'][i][z]:
                    print(f"{z}: {j} ")
            print()
            
            
        f.close()