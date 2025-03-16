
import type { DefineComponent, SlotsType } from 'vue'
type IslandComponent<T extends DefineComponent> = T & DefineComponent<{}, {refresh: () => Promise<void>}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, SlotsType<{ fallback: { error: unknown } }>>
interface _GlobalComponents {
      'SkeletonPost': typeof import("../components/SkeletonPost.vue")['default']
    'Comments': typeof import("../components/comments/Comments.vue")['default']
    'FormLogin': typeof import("../components/form/formLogin.vue")['default']
    'FormRegister': typeof import("../components/form/formRegister.vue")['default']
    'HeaderPage': typeof import("../components/headerPage.vue")['default']
    'LayoutAddPost': typeof import("../components/layout/addPost.vue")['default']
    'LayoutBurgerMenu': typeof import("../components/layout/burgerMenu.vue")['default']
    'LayoutFooter': typeof import("../components/layout/footer.vue")['default']
    'LayoutHeader': typeof import("../components/layout/header.vue")['default']
    'LayoutLoginButton': typeof import("../components/layout/loginButton.vue")['default']
    'LayoutLogo': typeof import("../components/layout/logo.vue")['default']
    'LayoutThemeSwitcher': typeof import("../components/layout/themeSwitcher.vue")['default']
    'PagePostCard': typeof import("../components/pagePost/pagePostCard.vue")['default']
    'PostActions': typeof import("../components/post/postActions.vue")['default']
    'PostAddComment': typeof import("../components/post/postAddComment.vue")['default']
    'PostCard': typeof import("../components/post/postCard.vue")['default']
    'PostComment': typeof import("../components/post/postComment.vue")['default']
    'PostComments': typeof import("../components/post/postComments.vue")['default']
    'PostContent': typeof import("../components/post/postContent.vue")['default']
    'PostHeader': typeof import("../components/post/postHeader.vue")['default']
    'UiButton': typeof import("../components/ui/button.vue")['default']
    'UiBaseInput': typeof import("../components/ui/uiBaseInput.vue")['default']
    'UiModal': typeof import("../components/ui/uiModal.vue")['default']
    'UserAvatar': typeof import("../components/user/userAvatar.vue")['default']
    'NuxtWelcome': typeof import("../node_modules/nuxt/dist/app/components/welcome.vue")['default']
    'NuxtLayout': typeof import("../node_modules/nuxt/dist/app/components/nuxt-layout")['default']
    'NuxtErrorBoundary': typeof import("../node_modules/nuxt/dist/app/components/nuxt-error-boundary")['default']
    'ClientOnly': typeof import("../node_modules/nuxt/dist/app/components/client-only")['default']
    'DevOnly': typeof import("../node_modules/nuxt/dist/app/components/dev-only")['default']
    'ServerPlaceholder': typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']
    'NuxtLink': typeof import("../node_modules/nuxt/dist/app/components/nuxt-link")['default']
    'NuxtLoadingIndicator': typeof import("../node_modules/nuxt/dist/app/components/nuxt-loading-indicator")['default']
    'NuxtRouteAnnouncer': typeof import("../node_modules/nuxt/dist/app/components/nuxt-route-announcer")['default']
    'NuxtImg': typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtImg.vue")['default']
    'NuxtPicture': typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtPicture.vue")['default']
    'NuxtLinkLocale': typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/NuxtLinkLocale")['default']
    'SwitchLocalePathLink': typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/SwitchLocalePathLink")['default']
    'SchemaOrgDebug': typeof import("@unhead/schema-org/vue")['SchemaOrgDebug']
    'SchemaOrgArticle': typeof import("@unhead/schema-org/vue")['SchemaOrgArticle']
    'SchemaOrgBreadcrumb': typeof import("@unhead/schema-org/vue")['SchemaOrgBreadcrumb']
    'SchemaOrgComment': typeof import("@unhead/schema-org/vue")['SchemaOrgComment']
    'SchemaOrgEvent': typeof import("@unhead/schema-org/vue")['SchemaOrgEvent']
    'SchemaOrgFoodEstablishment': typeof import("@unhead/schema-org/vue")['SchemaOrgFoodEstablishment']
    'SchemaOrgHowTo': typeof import("@unhead/schema-org/vue")['SchemaOrgHowTo']
    'SchemaOrgImage': typeof import("@unhead/schema-org/vue")['SchemaOrgImage']
    'SchemaOrgJobPosting': typeof import("@unhead/schema-org/vue")['SchemaOrgJobPosting']
    'SchemaOrgLocalBusiness': typeof import("@unhead/schema-org/vue")['SchemaOrgLocalBusiness']
    'SchemaOrgOrganization': typeof import("@unhead/schema-org/vue")['SchemaOrgOrganization']
    'SchemaOrgPerson': typeof import("@unhead/schema-org/vue")['SchemaOrgPerson']
    'SchemaOrgProduct': typeof import("@unhead/schema-org/vue")['SchemaOrgProduct']
    'SchemaOrgQuestion': typeof import("@unhead/schema-org/vue")['SchemaOrgQuestion']
    'SchemaOrgRecipe': typeof import("@unhead/schema-org/vue")['SchemaOrgRecipe']
    'SchemaOrgReview': typeof import("@unhead/schema-org/vue")['SchemaOrgReview']
    'SchemaOrgVideo': typeof import("@unhead/schema-org/vue")['SchemaOrgVideo']
    'SchemaOrgWebPage': typeof import("@unhead/schema-org/vue")['SchemaOrgWebPage']
    'SchemaOrgWebSite': typeof import("@unhead/schema-org/vue")['SchemaOrgWebSite']
    'SchemaOrgMovie': typeof import("@unhead/schema-org/vue")['SchemaOrgMovie']
    'SchemaOrgCourse': typeof import("@unhead/schema-org/vue")['SchemaOrgCourse']
    'SchemaOrgItemList': typeof import("@unhead/schema-org/vue")['SchemaOrgItemList']
    'SchemaOrgBook': typeof import("@unhead/schema-org/vue")['SchemaOrgBook']
    'SchemaOrgSoftwareApp': typeof import("@unhead/schema-org/vue")['SchemaOrgSoftwareApp']
    'Icon': typeof import("../node_modules/@nuxt/icon/dist/runtime/components/index")['default']
    'NuxtPage': typeof import("../node_modules/nuxt/dist/pages/runtime/page")['default']
    'NoScript': typeof import("../node_modules/nuxt/dist/head/runtime/components")['NoScript']
    'Link': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Link']
    'Base': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Base']
    'Title': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Title']
    'Meta': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Meta']
    'Style': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Style']
    'Head': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Head']
    'Html': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Html']
    'Body': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Body']
    'NuxtIsland': typeof import("../node_modules/nuxt/dist/app/components/nuxt-island")['default']
    'NuxtRouteAnnouncer': IslandComponent<typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']>
      'LazySkeletonPost': typeof import("../components/SkeletonPost.vue")['default']
    'LazyComments': typeof import("../components/comments/Comments.vue")['default']
    'LazyFormLogin': typeof import("../components/form/formLogin.vue")['default']
    'LazyFormRegister': typeof import("../components/form/formRegister.vue")['default']
    'LazyHeaderPage': typeof import("../components/headerPage.vue")['default']
    'LazyLayoutAddPost': typeof import("../components/layout/addPost.vue")['default']
    'LazyLayoutBurgerMenu': typeof import("../components/layout/burgerMenu.vue")['default']
    'LazyLayoutFooter': typeof import("../components/layout/footer.vue")['default']
    'LazyLayoutHeader': typeof import("../components/layout/header.vue")['default']
    'LazyLayoutLoginButton': typeof import("../components/layout/loginButton.vue")['default']
    'LazyLayoutLogo': typeof import("../components/layout/logo.vue")['default']
    'LazyLayoutThemeSwitcher': typeof import("../components/layout/themeSwitcher.vue")['default']
    'LazyPagePostCard': typeof import("../components/pagePost/pagePostCard.vue")['default']
    'LazyPostActions': typeof import("../components/post/postActions.vue")['default']
    'LazyPostAddComment': typeof import("../components/post/postAddComment.vue")['default']
    'LazyPostCard': typeof import("../components/post/postCard.vue")['default']
    'LazyPostComment': typeof import("../components/post/postComment.vue")['default']
    'LazyPostComments': typeof import("../components/post/postComments.vue")['default']
    'LazyPostContent': typeof import("../components/post/postContent.vue")['default']
    'LazyPostHeader': typeof import("../components/post/postHeader.vue")['default']
    'LazyUiButton': typeof import("../components/ui/button.vue")['default']
    'LazyUiBaseInput': typeof import("../components/ui/uiBaseInput.vue")['default']
    'LazyUiModal': typeof import("../components/ui/uiModal.vue")['default']
    'LazyUserAvatar': typeof import("../components/user/userAvatar.vue")['default']
    'LazyNuxtWelcome': typeof import("../node_modules/nuxt/dist/app/components/welcome.vue")['default']
    'LazyNuxtLayout': typeof import("../node_modules/nuxt/dist/app/components/nuxt-layout")['default']
    'LazyNuxtErrorBoundary': typeof import("../node_modules/nuxt/dist/app/components/nuxt-error-boundary")['default']
    'LazyClientOnly': typeof import("../node_modules/nuxt/dist/app/components/client-only")['default']
    'LazyDevOnly': typeof import("../node_modules/nuxt/dist/app/components/dev-only")['default']
    'LazyServerPlaceholder': typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']
    'LazyNuxtLink': typeof import("../node_modules/nuxt/dist/app/components/nuxt-link")['default']
    'LazyNuxtLoadingIndicator': typeof import("../node_modules/nuxt/dist/app/components/nuxt-loading-indicator")['default']
    'LazyNuxtRouteAnnouncer': typeof import("../node_modules/nuxt/dist/app/components/nuxt-route-announcer")['default']
    'LazyNuxtImg': typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtImg.vue")['default']
    'LazyNuxtPicture': typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtPicture.vue")['default']
    'LazyNuxtLinkLocale': typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/NuxtLinkLocale")['default']
    'LazySwitchLocalePathLink': typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/SwitchLocalePathLink")['default']
    'LazySchemaOrgDebug': typeof import("@unhead/schema-org/vue")['SchemaOrgDebug']
    'LazySchemaOrgArticle': typeof import("@unhead/schema-org/vue")['SchemaOrgArticle']
    'LazySchemaOrgBreadcrumb': typeof import("@unhead/schema-org/vue")['SchemaOrgBreadcrumb']
    'LazySchemaOrgComment': typeof import("@unhead/schema-org/vue")['SchemaOrgComment']
    'LazySchemaOrgEvent': typeof import("@unhead/schema-org/vue")['SchemaOrgEvent']
    'LazySchemaOrgFoodEstablishment': typeof import("@unhead/schema-org/vue")['SchemaOrgFoodEstablishment']
    'LazySchemaOrgHowTo': typeof import("@unhead/schema-org/vue")['SchemaOrgHowTo']
    'LazySchemaOrgImage': typeof import("@unhead/schema-org/vue")['SchemaOrgImage']
    'LazySchemaOrgJobPosting': typeof import("@unhead/schema-org/vue")['SchemaOrgJobPosting']
    'LazySchemaOrgLocalBusiness': typeof import("@unhead/schema-org/vue")['SchemaOrgLocalBusiness']
    'LazySchemaOrgOrganization': typeof import("@unhead/schema-org/vue")['SchemaOrgOrganization']
    'LazySchemaOrgPerson': typeof import("@unhead/schema-org/vue")['SchemaOrgPerson']
    'LazySchemaOrgProduct': typeof import("@unhead/schema-org/vue")['SchemaOrgProduct']
    'LazySchemaOrgQuestion': typeof import("@unhead/schema-org/vue")['SchemaOrgQuestion']
    'LazySchemaOrgRecipe': typeof import("@unhead/schema-org/vue")['SchemaOrgRecipe']
    'LazySchemaOrgReview': typeof import("@unhead/schema-org/vue")['SchemaOrgReview']
    'LazySchemaOrgVideo': typeof import("@unhead/schema-org/vue")['SchemaOrgVideo']
    'LazySchemaOrgWebPage': typeof import("@unhead/schema-org/vue")['SchemaOrgWebPage']
    'LazySchemaOrgWebSite': typeof import("@unhead/schema-org/vue")['SchemaOrgWebSite']
    'LazySchemaOrgMovie': typeof import("@unhead/schema-org/vue")['SchemaOrgMovie']
    'LazySchemaOrgCourse': typeof import("@unhead/schema-org/vue")['SchemaOrgCourse']
    'LazySchemaOrgItemList': typeof import("@unhead/schema-org/vue")['SchemaOrgItemList']
    'LazySchemaOrgBook': typeof import("@unhead/schema-org/vue")['SchemaOrgBook']
    'LazySchemaOrgSoftwareApp': typeof import("@unhead/schema-org/vue")['SchemaOrgSoftwareApp']
    'LazyIcon': typeof import("../node_modules/@nuxt/icon/dist/runtime/components/index")['default']
    'LazyNuxtPage': typeof import("../node_modules/nuxt/dist/pages/runtime/page")['default']
    'LazyNoScript': typeof import("../node_modules/nuxt/dist/head/runtime/components")['NoScript']
    'LazyLink': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Link']
    'LazyBase': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Base']
    'LazyTitle': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Title']
    'LazyMeta': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Meta']
    'LazyStyle': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Style']
    'LazyHead': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Head']
    'LazyHtml': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Html']
    'LazyBody': typeof import("../node_modules/nuxt/dist/head/runtime/components")['Body']
    'LazyNuxtIsland': typeof import("../node_modules/nuxt/dist/app/components/nuxt-island")['default']
    'LazyNuxtRouteAnnouncer': IslandComponent<typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']>
}

declare module 'vue' {
  export interface GlobalComponents extends _GlobalComponents { }
}

export const SkeletonPost: typeof import("../components/SkeletonPost.vue")['default']
export const Comments: typeof import("../components/comments/Comments.vue")['default']
export const FormLogin: typeof import("../components/form/formLogin.vue")['default']
export const FormRegister: typeof import("../components/form/formRegister.vue")['default']
export const HeaderPage: typeof import("../components/headerPage.vue")['default']
export const LayoutAddPost: typeof import("../components/layout/addPost.vue")['default']
export const LayoutBurgerMenu: typeof import("../components/layout/burgerMenu.vue")['default']
export const LayoutFooter: typeof import("../components/layout/footer.vue")['default']
export const LayoutHeader: typeof import("../components/layout/header.vue")['default']
export const LayoutLoginButton: typeof import("../components/layout/loginButton.vue")['default']
export const LayoutLogo: typeof import("../components/layout/logo.vue")['default']
export const LayoutThemeSwitcher: typeof import("../components/layout/themeSwitcher.vue")['default']
export const PagePostCard: typeof import("../components/pagePost/pagePostCard.vue")['default']
export const PostActions: typeof import("../components/post/postActions.vue")['default']
export const PostAddComment: typeof import("../components/post/postAddComment.vue")['default']
export const PostCard: typeof import("../components/post/postCard.vue")['default']
export const PostComment: typeof import("../components/post/postComment.vue")['default']
export const PostComments: typeof import("../components/post/postComments.vue")['default']
export const PostContent: typeof import("../components/post/postContent.vue")['default']
export const PostHeader: typeof import("../components/post/postHeader.vue")['default']
export const UiButton: typeof import("../components/ui/button.vue")['default']
export const UiBaseInput: typeof import("../components/ui/uiBaseInput.vue")['default']
export const UiModal: typeof import("../components/ui/uiModal.vue")['default']
export const UserAvatar: typeof import("../components/user/userAvatar.vue")['default']
export const NuxtWelcome: typeof import("../node_modules/nuxt/dist/app/components/welcome.vue")['default']
export const NuxtLayout: typeof import("../node_modules/nuxt/dist/app/components/nuxt-layout")['default']
export const NuxtErrorBoundary: typeof import("../node_modules/nuxt/dist/app/components/nuxt-error-boundary")['default']
export const ClientOnly: typeof import("../node_modules/nuxt/dist/app/components/client-only")['default']
export const DevOnly: typeof import("../node_modules/nuxt/dist/app/components/dev-only")['default']
export const ServerPlaceholder: typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']
export const NuxtLink: typeof import("../node_modules/nuxt/dist/app/components/nuxt-link")['default']
export const NuxtLoadingIndicator: typeof import("../node_modules/nuxt/dist/app/components/nuxt-loading-indicator")['default']
export const NuxtRouteAnnouncer: typeof import("../node_modules/nuxt/dist/app/components/nuxt-route-announcer")['default']
export const NuxtImg: typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtImg.vue")['default']
export const NuxtPicture: typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtPicture.vue")['default']
export const NuxtLinkLocale: typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/NuxtLinkLocale")['default']
export const SwitchLocalePathLink: typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/SwitchLocalePathLink")['default']
export const SchemaOrgDebug: typeof import("@unhead/schema-org/vue")['SchemaOrgDebug']
export const SchemaOrgArticle: typeof import("@unhead/schema-org/vue")['SchemaOrgArticle']
export const SchemaOrgBreadcrumb: typeof import("@unhead/schema-org/vue")['SchemaOrgBreadcrumb']
export const SchemaOrgComment: typeof import("@unhead/schema-org/vue")['SchemaOrgComment']
export const SchemaOrgEvent: typeof import("@unhead/schema-org/vue")['SchemaOrgEvent']
export const SchemaOrgFoodEstablishment: typeof import("@unhead/schema-org/vue")['SchemaOrgFoodEstablishment']
export const SchemaOrgHowTo: typeof import("@unhead/schema-org/vue")['SchemaOrgHowTo']
export const SchemaOrgImage: typeof import("@unhead/schema-org/vue")['SchemaOrgImage']
export const SchemaOrgJobPosting: typeof import("@unhead/schema-org/vue")['SchemaOrgJobPosting']
export const SchemaOrgLocalBusiness: typeof import("@unhead/schema-org/vue")['SchemaOrgLocalBusiness']
export const SchemaOrgOrganization: typeof import("@unhead/schema-org/vue")['SchemaOrgOrganization']
export const SchemaOrgPerson: typeof import("@unhead/schema-org/vue")['SchemaOrgPerson']
export const SchemaOrgProduct: typeof import("@unhead/schema-org/vue")['SchemaOrgProduct']
export const SchemaOrgQuestion: typeof import("@unhead/schema-org/vue")['SchemaOrgQuestion']
export const SchemaOrgRecipe: typeof import("@unhead/schema-org/vue")['SchemaOrgRecipe']
export const SchemaOrgReview: typeof import("@unhead/schema-org/vue")['SchemaOrgReview']
export const SchemaOrgVideo: typeof import("@unhead/schema-org/vue")['SchemaOrgVideo']
export const SchemaOrgWebPage: typeof import("@unhead/schema-org/vue")['SchemaOrgWebPage']
export const SchemaOrgWebSite: typeof import("@unhead/schema-org/vue")['SchemaOrgWebSite']
export const SchemaOrgMovie: typeof import("@unhead/schema-org/vue")['SchemaOrgMovie']
export const SchemaOrgCourse: typeof import("@unhead/schema-org/vue")['SchemaOrgCourse']
export const SchemaOrgItemList: typeof import("@unhead/schema-org/vue")['SchemaOrgItemList']
export const SchemaOrgBook: typeof import("@unhead/schema-org/vue")['SchemaOrgBook']
export const SchemaOrgSoftwareApp: typeof import("@unhead/schema-org/vue")['SchemaOrgSoftwareApp']
export const Icon: typeof import("../node_modules/@nuxt/icon/dist/runtime/components/index")['default']
export const NuxtPage: typeof import("../node_modules/nuxt/dist/pages/runtime/page")['default']
export const NoScript: typeof import("../node_modules/nuxt/dist/head/runtime/components")['NoScript']
export const Link: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Link']
export const Base: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Base']
export const Title: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Title']
export const Meta: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Meta']
export const Style: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Style']
export const Head: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Head']
export const Html: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Html']
export const Body: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Body']
export const NuxtIsland: typeof import("../node_modules/nuxt/dist/app/components/nuxt-island")['default']
export const NuxtRouteAnnouncer: IslandComponent<typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']>
export const LazySkeletonPost: typeof import("../components/SkeletonPost.vue")['default']
export const LazyComments: typeof import("../components/comments/Comments.vue")['default']
export const LazyFormLogin: typeof import("../components/form/formLogin.vue")['default']
export const LazyFormRegister: typeof import("../components/form/formRegister.vue")['default']
export const LazyHeaderPage: typeof import("../components/headerPage.vue")['default']
export const LazyLayoutAddPost: typeof import("../components/layout/addPost.vue")['default']
export const LazyLayoutBurgerMenu: typeof import("../components/layout/burgerMenu.vue")['default']
export const LazyLayoutFooter: typeof import("../components/layout/footer.vue")['default']
export const LazyLayoutHeader: typeof import("../components/layout/header.vue")['default']
export const LazyLayoutLoginButton: typeof import("../components/layout/loginButton.vue")['default']
export const LazyLayoutLogo: typeof import("../components/layout/logo.vue")['default']
export const LazyLayoutThemeSwitcher: typeof import("../components/layout/themeSwitcher.vue")['default']
export const LazyPagePostCard: typeof import("../components/pagePost/pagePostCard.vue")['default']
export const LazyPostActions: typeof import("../components/post/postActions.vue")['default']
export const LazyPostAddComment: typeof import("../components/post/postAddComment.vue")['default']
export const LazyPostCard: typeof import("../components/post/postCard.vue")['default']
export const LazyPostComment: typeof import("../components/post/postComment.vue")['default']
export const LazyPostComments: typeof import("../components/post/postComments.vue")['default']
export const LazyPostContent: typeof import("../components/post/postContent.vue")['default']
export const LazyPostHeader: typeof import("../components/post/postHeader.vue")['default']
export const LazyUiButton: typeof import("../components/ui/button.vue")['default']
export const LazyUiBaseInput: typeof import("../components/ui/uiBaseInput.vue")['default']
export const LazyUiModal: typeof import("../components/ui/uiModal.vue")['default']
export const LazyUserAvatar: typeof import("../components/user/userAvatar.vue")['default']
export const LazyNuxtWelcome: typeof import("../node_modules/nuxt/dist/app/components/welcome.vue")['default']
export const LazyNuxtLayout: typeof import("../node_modules/nuxt/dist/app/components/nuxt-layout")['default']
export const LazyNuxtErrorBoundary: typeof import("../node_modules/nuxt/dist/app/components/nuxt-error-boundary")['default']
export const LazyClientOnly: typeof import("../node_modules/nuxt/dist/app/components/client-only")['default']
export const LazyDevOnly: typeof import("../node_modules/nuxt/dist/app/components/dev-only")['default']
export const LazyServerPlaceholder: typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']
export const LazyNuxtLink: typeof import("../node_modules/nuxt/dist/app/components/nuxt-link")['default']
export const LazyNuxtLoadingIndicator: typeof import("../node_modules/nuxt/dist/app/components/nuxt-loading-indicator")['default']
export const LazyNuxtRouteAnnouncer: typeof import("../node_modules/nuxt/dist/app/components/nuxt-route-announcer")['default']
export const LazyNuxtImg: typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtImg.vue")['default']
export const LazyNuxtPicture: typeof import("../node_modules/@nuxt/image/dist/runtime/components/NuxtPicture.vue")['default']
export const LazyNuxtLinkLocale: typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/NuxtLinkLocale")['default']
export const LazySwitchLocalePathLink: typeof import("../node_modules/@nuxtjs/i18n/dist/runtime/components/SwitchLocalePathLink")['default']
export const LazySchemaOrgDebug: typeof import("@unhead/schema-org/vue")['SchemaOrgDebug']
export const LazySchemaOrgArticle: typeof import("@unhead/schema-org/vue")['SchemaOrgArticle']
export const LazySchemaOrgBreadcrumb: typeof import("@unhead/schema-org/vue")['SchemaOrgBreadcrumb']
export const LazySchemaOrgComment: typeof import("@unhead/schema-org/vue")['SchemaOrgComment']
export const LazySchemaOrgEvent: typeof import("@unhead/schema-org/vue")['SchemaOrgEvent']
export const LazySchemaOrgFoodEstablishment: typeof import("@unhead/schema-org/vue")['SchemaOrgFoodEstablishment']
export const LazySchemaOrgHowTo: typeof import("@unhead/schema-org/vue")['SchemaOrgHowTo']
export const LazySchemaOrgImage: typeof import("@unhead/schema-org/vue")['SchemaOrgImage']
export const LazySchemaOrgJobPosting: typeof import("@unhead/schema-org/vue")['SchemaOrgJobPosting']
export const LazySchemaOrgLocalBusiness: typeof import("@unhead/schema-org/vue")['SchemaOrgLocalBusiness']
export const LazySchemaOrgOrganization: typeof import("@unhead/schema-org/vue")['SchemaOrgOrganization']
export const LazySchemaOrgPerson: typeof import("@unhead/schema-org/vue")['SchemaOrgPerson']
export const LazySchemaOrgProduct: typeof import("@unhead/schema-org/vue")['SchemaOrgProduct']
export const LazySchemaOrgQuestion: typeof import("@unhead/schema-org/vue")['SchemaOrgQuestion']
export const LazySchemaOrgRecipe: typeof import("@unhead/schema-org/vue")['SchemaOrgRecipe']
export const LazySchemaOrgReview: typeof import("@unhead/schema-org/vue")['SchemaOrgReview']
export const LazySchemaOrgVideo: typeof import("@unhead/schema-org/vue")['SchemaOrgVideo']
export const LazySchemaOrgWebPage: typeof import("@unhead/schema-org/vue")['SchemaOrgWebPage']
export const LazySchemaOrgWebSite: typeof import("@unhead/schema-org/vue")['SchemaOrgWebSite']
export const LazySchemaOrgMovie: typeof import("@unhead/schema-org/vue")['SchemaOrgMovie']
export const LazySchemaOrgCourse: typeof import("@unhead/schema-org/vue")['SchemaOrgCourse']
export const LazySchemaOrgItemList: typeof import("@unhead/schema-org/vue")['SchemaOrgItemList']
export const LazySchemaOrgBook: typeof import("@unhead/schema-org/vue")['SchemaOrgBook']
export const LazySchemaOrgSoftwareApp: typeof import("@unhead/schema-org/vue")['SchemaOrgSoftwareApp']
export const LazyIcon: typeof import("../node_modules/@nuxt/icon/dist/runtime/components/index")['default']
export const LazyNuxtPage: typeof import("../node_modules/nuxt/dist/pages/runtime/page")['default']
export const LazyNoScript: typeof import("../node_modules/nuxt/dist/head/runtime/components")['NoScript']
export const LazyLink: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Link']
export const LazyBase: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Base']
export const LazyTitle: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Title']
export const LazyMeta: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Meta']
export const LazyStyle: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Style']
export const LazyHead: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Head']
export const LazyHtml: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Html']
export const LazyBody: typeof import("../node_modules/nuxt/dist/head/runtime/components")['Body']
export const LazyNuxtIsland: typeof import("../node_modules/nuxt/dist/app/components/nuxt-island")['default']
export const LazyNuxtRouteAnnouncer: IslandComponent<typeof import("../node_modules/nuxt/dist/app/components/server-placeholder")['default']>

export const componentNames: string[]
