if !filereadable($HOME.'/.vim/autoload/plug.vim')
  !curl -fLo ~/.vim/autoload/plug.vim --create-dirs 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  source $MYVIMRC
else
  call plug#begin('~/.vim/plugins')
    Plug 'airblade/vim-gitgutter'
    Plug 'aonemd/kuroi.vim'  " A very dark colorscheme for Vim. JOIN THE DARK SIDE!
    Plug 'davidhalter/jedi-vim'
    Plug 'dense-analysis/ale'
    Plug 'dracula/vim', { 'as': 'dracula' }
    Plug 'github/copilot.vim'
    Plug 'godlygeek/tabular'
    Plug 'hashivim/vim-terraform'
    Plug 'joshdick/onedark.vim'
    Plug 'juliosueiras/vim-terraform-completion'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/goyo.vim'
    Plug 'machakann/vim-sandwich'
    Plug 'mileszs/ack.vim'
    Plug 'preservim/tagbar'                           " Vim plugin that displays tags in a window, ordered by scope -- https://preservim.github.io/tagbar
    Plug 'sheerun/vim-polyglot'                       " configured in file ftplugins/python.vim
    Plug 'simnalamburt/vim-mundo'
    Plug 'terryma/vim-multiple-cursors'
    Plug 'tpope/vim-commentary'
    Plug 'tpope/vim-fugitive'
  call plug#end()

  set autoindent                                     " always set autoindenting on
  set autoread                                       " automatically read changes in the file
  set background=dark
  set backspace=indent,eol,start                     " make backspace behave properly in insert mode
  set colorcolumn=80                                 " display text width column
  set completeopt=longest,menuone,preview            " better insert mode completions
  set cursorline                                     " highlight current line
  set cursorcolumn                                   " highlight current column
  "set formatoptions-=cro                             " disable auto comments on new lines
  set hidden                                         " hide buffers instead of closing them even if they contain unwritten changes
  set hlsearch                                       " highlight search patterns
  set ignorecase                                     " searches are case insensitive...
  set incsearch                                      " incremental search highlight
  set laststatus=2                                   " always display the status bar
  set lazyredraw                                     " lazily redraw screen while executing macros, and other commands
  set mouse=a                                        " disable the mouse support
  set noswapfile                                     " disable swap files
  set nowrap                                         " disable soft wrap for lines
  set number                                         " display line numbers
  set scrolloff=2                                    " always show 2 lines above/below the cursor
  set showcmd                                        " display incomplete commands
  set smartcase                                      " ...unless they contain at least one capital letter
  set splitbelow                                     " vertical splits will be at the bottom
  set splitright                                     " horizontal splits will be to the right
  set statusline=%=%m\ %c\ %P\ %f                    " status line: modifiedflag, charcount, filepercent, filepath
  set tabstop=4 shiftwidth=4 softtabstop=4 expandtab " use four spaces for indentation
  set t_Co=256                                       " enable 256 colors
  set ttimeoutlen=50                                 "  ...makes for a faster key response
  set ttimeout                                       " time waited for key press(es) to complete...
  set ttyfast                                        " more characters will be sent to the screen for redrawing
  set wildmenu                                       " better menu with completion in command mode
  set wildmode=longest:full,full
  " https://www.perplexity.ai/search/f6441c47-4761-4c1a-825d-b68fdce9c575
  set exrc                                           " permet à Vim de rechercher et de charger un fichier .vimrc dans le répertoire courant
  set secure                                         " garantit que seules les options sûres sont autorisées dans les fichiers .vimrc locaux

  if system('uname -s') == "Darwin\n"
      set clipboard=unnamed "OSX
  else
      set clipboard=unnamedplus "Linux
  endif

  colorscheme evening
  " colorscheme dracula

  autocmd! FileType c    setlocal ts=4 sts=4 sw=4 noexpandtab
  autocmd! FileType java setlocal ts=4 sts=4 sw=4 expandtab
  autocmd! FileType make setlocal ts=8 sts=8 sw=8 noexpandtab
  autocmd! FileType html setlocal ts=2 sts=2 sw=2 noexpandtab
  autocmd! FileType css  setlocal ts=2 sts=2 sw=2 noexpandtab
  autocmd! FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

  "remove current line highlight in unfocused window
  au VimEnter,WinEnter,BufWinEnter,FocusGained,CmdwinEnter * set cul
  au WinLeave,FocusLost,CmdwinLeave * set nocul

  "remove trailing whitespace on save
  autocmd! BufWritePre * :%s/\s\+$//e

  "The Leader
  let mapleader=","

  nnoremap ! :!
  nnoremap <leader>w :w<cr>
  "replace the word under cursor
  nnoremap <leader>* :%s/\<<c-r><c-w>\>//g<left><left>
  "toggle showing hidden characters
  nnoremap <silent> <leader>s :set nolist!<cr>
  "toggle spell checking
  nnoremap <leader>ss :setlocal spell!<cr>
  "toggle RTL mode
  nnoremap <silent> <leader>l :set rl!<cr>
  "override system files by typing :w!!
  cnoremap w!! %!sudo tee > /dev/null %
  "remove search highlight
  nmap <leader>q :nohlsearch<CR>
  "jsonify the avro selected_data retrieved from CCC
  nnoremap <leader>m :%s/\s{\n\s*"\(int\\|long\\|string\\|boolean\)": \(.*\)\n\s*}/ \2/g<cr>
  " Base64 'e'ncode and 'd'ecode
  vnoremap <leader>64 c<c-r>=system('base64 --decode', @")<cr><esc>
  " Ce code crée un groupe d'événements nommé myvimrc qui surveille les
  " modifications apportées à votre fichier de configuration et recharge
  " automatiquement la configuration lorsque le fichier est enregistré.
  augroup myvimrc
    au!
    au BufWritePost .vimrc,_vimrc,vimrc,.gvimrc,_gvimrc,gvimrc so $MYVIMRC | if has('gui_running') | so $MYGVIMRC | endif
  augroup END

  "move lines around
  nnoremap <leader>k :m-2<cr>==
  xnoremap <leader>j :m'>+<cr>gv=gv
  xnoremap <leader>k :m-2<cr>gv=gv
  nnoremap <leader>j :m+<cr>==

  " Mise en surbrillance du mot sous le cursor sans lancer une recherche
  " d'occurrence
  let g:highlight_enabled = 0
  nnoremap <leader>h :if g:highlight_enabled == 0<CR>
             \let @/=expand("<cword>")<CR>
             \:match Search /<C-R>///><CR>
             \let g:highlight_enabled = 1<CR>
           \else<CR>
             \:match none<CR>
             \let g:highlight_enabled = 0<CR>
           \endif<CR>


  "keep text selected after indentation
  vnoremap < <gv
  vnoremap > >gv

  "fzf
  nnoremap <leader>p :FZF<cr>
  nnoremap <leader>o :Lines<cr>
  nnoremap <leader>t :Tags<cr>
  nnoremap <leader>r :Buffers<cr>

  " Ack / Ag
  if executable('ag')
    let g:ackprg = 'ag --vimgrep --skip-vcs-ignores'
  endif

  "Ctags
  set tags+=.git/tags
  nnoremap <leader>ct :!ctags -Rf .git/tags --tag-relative --extras=+f --exclude=.git,pkg,__pycache__,.pytest_cache --languages=-sql<cr><cr>

  " Mundo
  " A git mirror of mundo.vim
  let g:mundo_width = 60
  let g:mundo_preview_height = 40
  let g:mundo_right = 1
  set undofile
  set undolevels=4000
  " Crée le répertoire undodir s'il n'existe pas
  if !isdirectory(expand("~/.vim/undo"))
    " L'argument 'p' utilisé avec mkdir() permet de créer les répertoires parents si nécessaire.
    call mkdir(expand("~/.vim/undo"), "p")
  endif
  set undodir=~/.vim/undo
  nnoremap <F5> :MundoToggle<CR>

  "GitGutter
  autocmd BufWritePost * GitGutter
  nnoremap <c-N> :GitGutterNextHunk<CR>
  nnoremap <c-P> :GitGutterPrevHunk<CR>
  nnoremap <c-U> :GitGutterUndoHunk<CR>
  nnoremap <leader>B :enew<cr>
  nnoremap <Tab> :bnext<cr>
  nnoremap <S-Tab> :bprevious<cr>
  nnoremap <leader>bq :bp <bar> bd! #<cr>
  nnoremap <leader>ba :bufdo bd!<cr>
  "cycle between last two open buffers
  nnoremap <leader><leader> <c-^>
  function! GitStatus()
    let [a,m,r] = GitGutterGetHunkSummary()
    return printf(' +%d ~%d -%d', a, m, r)
  endfunction
  set statusline+=%{GitStatus()}

  "netrw
  let g:netrw_altv = 1
  let g:netrw_banner = 0
  let g:netrw_browse_split = 4
  let g:netrw_liststyle = 3
  let g:netrw_localrmdir = 'rm -rf'
  let g:netrw_winsize = 25
  nnoremap <leader>n :Lexplore<CR>

  "move to the split in the direction shown, or create a new split
  nnoremap <silent> <C-h> :call WinMove('h')<cr>
  nnoremap <silent> <C-j> :call WinMove('j')<cr>
  nnoremap <silent> <C-k> :call WinMove('k')<cr>
  nnoremap <silent> <C-l> :call WinMove('l')<cr>
  function! WinMove(key)
    let t:curwin = winnr()
    exec "wincmd ".a:key
    if (t:curwin == winnr())
      if (match(a:key,'[jk]'))
        wincmd v
      else
        wincmd s
      endif
      exec "wincmd ".a:key
    endif
  endfunction

  "Goyo
  nnoremap <leader>g :Goyo<cr>
  if !exists('*s:goyo_leave')
    function s:goyo_leave()
      source $MYVIMRC
    endfunction
  endif
  autocmd! User GoyoLeave nested call <SID>goyo_leave()

  " Tabularize
  if exists(":Tabularize")
      nmap <Leader>a= :Tabularize /=<CR>
      vmap <Leader>a= :Tabularize /=<CR>
      nmap <Leader>a: :Tabularize /:\zs<CR>
      vmap <Leader>a: :Tabularize /:\zs<CR>
  endif

  " Tagbar
  " Look also the <Leader>t from the fzf plugin see above !
  nmap <F8> :TagbarToggle<CR>

  " ALE: Asynchronous Lint Engine
  let g:ale_open_list = 0
  let g:ale_keep_list_window_open = 0
  let g:ale_sign_error = "🚨"
  let g:ale_sign_warning = "🚧"
  let g:ale_fixers = {
  \   '*': ['remove_trailing_lines', 'trim_whitespace'],
  \   'python': ['black', 'isort'],
  \}
  " Set this variable to 1 to fix files when you save them.
  let g:ale_fix_on_save = 1
  let g:ale_python_auto_virtualenv=1
  let g:ale_python_isort_executable = 'python3'
  let g:ale_python_isort_options = '-m isort --profile black'
  let g:ale_python_black_executable = 'python3'
  let g:ale_python_black_options = '-m black --line-length 120 --target-version py310'
  let g:ale_python_flake8_executable = 'python3'
  let g:ale_python_flake8_options = '-m flake8 --ignore=E501,W6'

  " Zoom / Restore window.
  " A vim function to zoom in on a single split window and restore the previous layout.
  function! s:ZoomToggle() abort
      if exists('t:zoomed') && t:zoomed
          execute t:zoom_winrestcmd
          let t:zoomed = 0
      else
          let t:zoom_winrestcmd = winrestcmd()
          resize
          vertical resize
          let t:zoomed = 1
      endif
  endfunction
  command! ZoomToggle call s:ZoomToggle()
  noremap <silent> <Leader>z :ZoomToggle<CR>

  " Python AutoComplete
  " Plug 'davidhalter/jedi-vim'
  " I don't want the docstring window to popup during completion
  " This depends on the completeopt option. Jedi initializes it in its ftplugin.
  " Add the following line to your .vimrc to disable it:
  autocmd FileType python setlocal completeopt-=preview
  let g:jedi#popup_select_first = 0
  let g:jedi#show_call_signatures = "1"
  " NOTE: subject to change!
  let g:jedi#goto_command = "<leader>d"
  " let g:jedi#goto_assignments_command = "<leader>g"  " Already mapped
  let g:jedi#goto_stubs_command = "<leader>s"
  let g:jedi#goto_definitions_command = "<leader>G"
  let g:jedi#documentation_command = "K"
  " let g:jedi#usages_command = "<leader>n"  " Already mapped
  let g:jedi#completions_command = "<C-Space>"
  let g:jedi#rename_command = "<leader>r"
  let g:jedi#rename_command_keep_name = "<leader>R"

endif
