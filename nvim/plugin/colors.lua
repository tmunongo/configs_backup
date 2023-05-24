function ColorMyPencils(color)
	color = color or "tokyonight"
	vim.cmd.colorscheme(color)

	vim.api.nvim_set_hl(0, "Normal", {  })
	vim.api.nvim_set_hl(0, "NormalFloat", {  })
	

end

--ColorMyPencils()
