import re
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multiplanet
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""
tokens = re.findall("[\w']+", text)
print(tokens)
