"=============================================================================
" File: comfortablecpp.vim
" Author: AtsushiSakai
" Created: 2015-07-25
"=============================================================================

scriptencoding utf-8

if !exists('g:loaded_comfortablecpp')
    finish
endif
let g:loaded_comfortablecpp = 1

let s:save_cpo = &cpo
set cpo&vim

"get filepath
let g:path_comfortablecpp=expand("<sfile>:p:h:h")

function! comfortablecpp#Comfortablecpp_GenerateShowStructFunction()
  "Get selected code with visual mode
  let tmp = @@
  silent normal gvy
  let selected = @@
  let @@ = tmp
  
  "echo selected
  py import sys
  py import vim
  py sys.argv = vim.eval("selected")
  let fullpath=g:path_comfortablecpp."/autoload/GenerateShowStructFunction.py"
  execute 'pyfile '.fullpath
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
