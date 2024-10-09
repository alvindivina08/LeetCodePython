sentence = "Hello, world!"

def countString(string):
    count = {}

    for n in string:
        if n.isalnum():
            count[n] = count.get(n, 0) + 1

    return count

result = countString(sentence)

print(result)

json = {
    "fruits": ["apple", "orange", "banana"],
    "vegetables": ["onion", "bell pepper"]
}

def addData(jsonDoc, key, item):

    if key in jsonDoc:
        jsonDoc[key].append(item)
    else:
        jsonDoc[key] = [item]

    return jsonDoc

result = addData(json, 'yeet', 'potato')
result = addData(json, 'yeet', 'jingle bells')


print(result)