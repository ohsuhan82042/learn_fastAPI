<script>
  import {link} from 'svelte-spa-router'
  import { page, access_token, username, is_login, real_username } from "../lib/store"
</script>
<!-- 네이게이션 바 -->
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
  <div class="container-fluid">
    <a use:link class="navbar-brand" href="/" on:click="{()=>{$page=0}}">머먹고 살지</a>
    <button
          class="navbar-toggler"
          type='button'
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent" 
          aria-controls="navbarSupportedContent" 
          aria-expanded="false" 
          aria-label="Toggle navigation">
          <span class ="navbar-toggler-icon"/>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0"> 
            {#if $is_login }
              <li class="nav-item">
                <a use:link href="/user-login" class="nav-link" on:click
                ={() => {
                $access_token = ''
                $username = ''
                $is_login = false
                $real_username = ''
                }}>로그아웃 ({$real_username}님 안녕하세요)</a>              </li>
            {:else}
              <li class="nav-item">
                <a use:link class="nav-link" href="/user-create">회원 가입</a>
              </li>
              <li class="nav-item">
                <a use:link class="nav-link" href="/user-login">로그인</a>
              </li>
            {/if}
        </ul>
      </div>
  </div>
</nav>