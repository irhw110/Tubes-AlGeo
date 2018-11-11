def translate (vertices,a,b) :
    translasi = []
    for i in range (len(vertices)) :
        translasi.append([a,b,0])

    for i in range (len(vertices)) :
        vertices[i][0] = vertices[i][0] + translasi[i][0]
        vertices[i][1] = vertices[i][1] + translasi[i][1]
    return vertices
