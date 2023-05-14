// .vuepress/config.js

const getSidebar = require('./get_sidebar.js');


module.exports={
    base: "/minecraft-modpack-enigmatica-8-diary/",
    // title: "Minecraft Modpack Guide",
    // description: "Ultimite Guide for minecraft modpack's general guide & tips",

    plugins: [
        ['vuepress-plugin-redirect', 
          {
          // provide i18n redirection
          // it will automatically redirect `/foo/bar/` to `/:locale/foo/bar/` if exists
          locales: true,
          }
        ],
        '@vuepress/back-to-top',
        "@vuepress/last-updated",
        "vuepress-plugin-code-copy",
        '@vuepress/medium-zoom',
        '@vuepress/nprogress'//,
        // [
        // 'vuepress-plugin-right-anchor',
        // {
        //   expand: {
        //     clickModeDefaultOpen: false,
        //     trigger: 'click'
        //   },
        // }
        // ]
    ],
    locales:{
        '/Ko/': {
            lang: 'ko-KR', // this will set as the land attibute on <html>
            title: "Our Enigmatica-8 Server!",
            description: "Our diary of Enigmatica-8 server"
        },

        // '/En/': {
        //     lang: 'en-US',
        //     title: "Our Enigmatica-8 Server!",
        //     description: "Our diary of Enigmatica-8 server"
        // }
    },
    themeConfig: {
        hb_version: 'latest',
        sidebarDepth: 2,
        searchMaxSuggestions: 20,
        lastUPdated: "Last Updated",

        locales:{
            //Ko
            '/Ko/': {
                // text for the languege dropdown
                selectText: "Languages",
                // Label for this local in the language dropdown
                label: '한국어',
                // Aria Label for local in the dropdown
                ariaLabel: 'Languages',
                // test for the edit-on-github-link
                editLinkText: 'Edit this page on GitHub',
                serviceWorker: {
                    updatePopup:{
                        message: "New content is available.",
                        buttonText: "Refresh"
                    }
                },
                nav:[
                    {
                        text: 'Ko',
                        ariaLabel: 'Google',
                        items: [
                            {text: 'Website', link: 'https://google.com/', ariaLabel: 'Website Link'}
                        ]
                    },
                ],
                sidebar:{
                    '/Ko/': getSidebar.sidebar('Ko')
                }
            },

            // //En
            // '/En/': {
            //     // text for the languege dropdown
            //     selectText: "Languages",
            //     // Label for this local in the language dropdown
            //     label: 'English',
            //     // Aria Label for local in the dropdown
            //     ariaLabel: 'Languages',
            //     // test for the edit-on-github-link
            //     editLinkText: 'Edit this page on GitHub',
            //     serviceWorker: {
            //         updatePopup:{
            //             message: "New content is available.",
            //             buttonText: "Refresh"
            //         }
            //     },
            //     nav:[
            //         {
            //             text: 'Ko',
            //             ariaLabel: 'Test google',
            //             items: [
            //                 {text: 'Website', link: 'https://google.com/', ariaLabel: 'Website Link'}
            //             ]
            //         }
            //     ],
            //     sidebar:{
            //         '/En/': getSidebar.sidebar('En')
            //     }
            // }
        }
    }
}