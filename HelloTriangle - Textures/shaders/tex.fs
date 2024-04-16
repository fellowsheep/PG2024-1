#version 400

in vec3 vertexColor;
in vec2 texcoord;

uniform sampler2D texBuffer;

out vec4 color;
void main()
{
	color = texture(texBuffer, texcoord);//vec4(vertexColor,1.0);

}