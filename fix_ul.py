with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

bad = """                    </div></div>
                </div>
              </div>
              <li>Amrutha</li>"""

good = """                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <ul class="list-disc pl-4 space-y-1 text-gray-300 max-h-48 overflow-y-auto custom-scrollbar text-xs">
              <li>Aaradhana</li>
              <li>Amrutha</li>"""

content = content.replace(bad, good)
with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("fixed ul")
