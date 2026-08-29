with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace(r"'\uF04E\uF0FE\uF0E7'", r"'\uF04E\uF0E7'")
content = content.replace(r"'\uF04E\uF0FE\uF0E7\uF07A'", r"'\uF04E\uF0E7\uF07A'")
content = content.replace(r"'\uF04E\uF0FE\uF0E7\uF07B'", r"'\uF04E\uF0E7\uF07B'")
content = content.replace(r"'\uF04E\uF0FE\uF0E7\uF07D'", r"'\uF04E\uF0E7\uF07D'")
content = content.replace(r"'\uF04E\uF0FE\uF079'", r"'\uF04E\uF079'")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
