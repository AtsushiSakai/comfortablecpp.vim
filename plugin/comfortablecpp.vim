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



let &cpo = s:save_cpo
unlet s:save_cpo
