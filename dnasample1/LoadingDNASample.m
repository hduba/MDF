dm3struct = DM3Import('dnasample1.dm3');
N = length( dm3struct.image_data );
image = imagesc( (1:N).*dm3struct.xaxis.scale, (1:N).*dm3struct.yaxis.scale, ...
dm3struct.image_data.*dm3struct.intensity.scale );
axis off;

saveas(image, "dna_rbg.png")

RBG = imread("dna_rbg.png");
imshow(RBG);

I = rgb2gray(RBG);
fig = figure;
imshow(I);

saveas(fig, "dna_gray.png")