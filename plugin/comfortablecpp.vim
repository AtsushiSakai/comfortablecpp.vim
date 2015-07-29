"=============================================================================
" File: comfortablecpp.vim
" Author: AtsushiSakai
" Created: 2015-07-25
"=============================================================================

scriptencoding utf-8

if exists('g:loaded_comfortablecpp')
    finish
endif
let g:loaded_comfortablecpp = 1

let s:save_cpo = &cpo
set cpo&vim

" Command enable
vmap <silent> cps :<C-U>call comfortablecpp#Comfortablecpp_GenerateShowStructFunction()<CR>


let &cpo = s:save_cpo
unlet s:save_cpo
