local function main(p)
    setup_device(p)-- get dtype
	setup_images(p)-- get init_image, content_image, style_image
	setup_network_1(p)-- get row network
	setup_network_2(p)-- insert loss layer
	train(p)
end
local p = cmd:parse(arg)
p.output_image = string.format("%s/res.%s",paths.dirname(p.content_image),paths.extname(p.content_image))
main(p)
