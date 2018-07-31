import Algorithmia

input = {
    "input":
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/STOP_sign.jpg/220px-STOP_sign.jpg",
    "output": "data://.algo/character_recognition/TextDetectionCTPN/temp/receipt.png"
}
client = Algorithmia.client('simQubrq3ubzM21MWS71oDvbR011')
algo = client.algo('character_recognition/TextDetectionCTPN/0.2.0')
print(algo.pipe(input).result)
