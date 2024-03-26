#version 400

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;

out vec3 vertexColor;

void main()
{
	vertexColor = color;
	//...pode ter mais linhas de código aqui!
	gl_Position = vec4(position.x, position.y, position.z, 1.0);
}