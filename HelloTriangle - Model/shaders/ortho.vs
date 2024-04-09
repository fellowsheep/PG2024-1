#version 400

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;

out vec3 vertexColor;

uniform mat4 projection;
uniform mat4 model;

void main()
{
	vertexColor = color;
	//...pode ter mais linhas de código aqui!
	gl_Position = projection * model * vec4(position, 1.0);
}