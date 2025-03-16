<template>
    <div class="skeleton">
        <div class="skeleton__logo">
            <span></span>
        </div>
        <div class="skeleton__content">
            <div class="skeleton__title"></div>
            <div class="skeleton__text"></div>
            <div class="skeleton__text"></div>
        </div>
    </div>
</template>

<style lang="scss">
.skeleton {
    display: flex;
    gap: 20px;
    width: 100%;
    border-radius: 8px;
    padding: 20px;

    &__logo {
        display: flex;
        justify-content: center;

        height: 100%;
        span {
            display: block;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: #ccc;
            animation: pulse 1.5s infinite ease-in-out;
        }
    }

    &__content {
        display: flex;
        flex-direction: column;
        gap: 10px;

        width: 100%;
    }

    &__title {
        display: block;
        width: 40%;
        height: 15px;
        background: var(--first-skeleton);
        border-radius: 8px;
        animation: pulse 1.5s infinite ease-in-out;
    }

    &__text {
        display: block;
        width: 100%;
        height: 15px;
        background: var(--first-skeleton);
        border-radius: 8px;
        animation: pulse 1.5s infinite ease-in-out;

        &:last-child {
            width: 80%;
        }
    }
}

@keyframes pulse {
    0% {
        background-color: var(--second-skeleton);
    }
    50% {
        background-color: var(--first-skeleton);
    }
    100% {
        background-color: var(--second-skeleton);
    }
}
</style>
