<template>
    <div class="empty__page">
        <slot />
    </div>
</template>

<style lang="scss">
.empty__page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-grow: 1;

    width: 100%;
    min-height: 100vh;

    background-color: var(--primary-bg);
    background: url(../assets/img/bg_auth.svg);
    background-size: cover;
    background-position: top center;
    background-repeat: no-repeat;
}
</style>
