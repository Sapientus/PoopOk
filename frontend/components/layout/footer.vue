<script setup lang="ts">
import {useI18n} from 'vue-i18n';

const {t} = useI18n();
const currentYear = new Date().getFullYear();
</script>

<template>
    <footer class="footer">
        <p class="footer__year">{{ t("year", {year: currentYear}) }}</p>
        <ul class="footer__list">
            <li class="footer__item">
                <a href="#">{{ t("terms") }}</a>
            </li>
            <li class="footer__item">
                <a href="#">{{ t("privacy") }}</a>
            </li>
            <li class="footer__item">
                <a href="#">{{ t("cookie") }}</a>
            </li>
            <li class="footer__item">
                <a>{{ t("report") }}</a>
            </li>
        </ul>
    </footer>
</template>

<style lang="scss">
.footer {
    display: flex;
    align-items: center;
    justify-content: center;

    margin-left: 100px;
    padding: 30px 0 15px 0;

    background-color: var(--primary-bg);

    color: var(--primary-text);

    &__year {
        margin-right: 20px;

        font-size: 14px;
    }

    &__list {
        display: flex;
        justify-content: center;
        gap: 10px;

        list-style: none;
    }

    &__item {
        font-size: 14px;
    }
}
</style>
