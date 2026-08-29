with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace("'का': '\uF04E\uF0FE\uF0E7'", "'का': '\uF04E\uF0E7'")
content = content.replace("'को': '\uF04E\uF0FE\uF0E7\uF07A'", "'को': '\uF04E\uF0E7\uF07A'")
content = content.replace("'कौ': '\uF04E\uF0FE\uF0E7\uF07B'", "'कौ': '\uF04E\uF0E7\uF07B'")
content = content.replace("'कॉ': '\uF04E\uF0FE\uF0E7\uF07D'", "'कॉ': '\uF04E\uF0E7\uF07D'")
content = content.replace("'की': '\uF04E\uF0FE\uF079'", "'की': '\uF04E\uF079'")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
