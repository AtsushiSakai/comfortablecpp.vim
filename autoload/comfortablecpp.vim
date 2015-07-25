"=============================================================================
" File: comfortablecpp.vim
" Author: AtsushiSakai
" Created: 2015-07-25
"=============================================================================

scriptencoding utf-8

""if !exists('g:loaded_comfortablecpp')
""    finish
""endif
""let g:loaded_comfortablecpp = 1

let s:save_cpo = &cpo
set cpo&vim

""function! bookmarklet#GenerateBookmarklet()
function! Comfortablecpp_GenerateShowStructFunction()
  "Get selected code with visual mode
  let tmp = @@
  silent normal gvy
  let selected = @@
  let @@ = tmp
  
  "echo selected
  py import sys
  py import vim
  py sys.argv = vim.eval("selected")
  pyfile GenerateShowStructFunction.py

endfunction

" Command enable
command! -nargs=0 GenerateShowStructFunction :<C-U>call Comfortablecpp_GenerateShowStructFunction()
vmap <silent> ssf :<C-U>call Comfortablecpp_GenerateShowStructFunction()<CR>

let &cpo = s:save_cpo
unlet s:save_cpo
