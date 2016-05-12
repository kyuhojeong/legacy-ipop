
{
  'targets': [
    {
      'target_name': 'ipop-tap',
      'type': 'static_library',
      'sources': [
        '../legacy-ipop/ipop-tap/src/headers.c',
        '../legacy-ipop/ipop-tap/src/headers.h',
        '../legacy-ipop/ipop-tap/src/packetio.c',
        '../legacy-ipop/ipop-tap/src/packetio.h',
        '../legacy-ipop/ipop-tap/src/peerlist.c',
        '../legacy-ipop/ipop-tap/src/peerlist.h',
        '../legacy-ipop/ipop-tap/src/socket_utils.c',
        '../legacy-ipop/ipop-tap/src/socket_utils.h',
        '../legacy-ipop/ipop-tap/src/tap.c',
        '../legacy-ipop/ipop-tap/src/tap.h',
        '../legacy-ipop/ipop-tap/src/win32_tap.c',
        '../legacy-ipop/ipop-tap/src/win32_tap.h',
        '../legacy-ipop/ipop-tap/src/translator.c',
        '../legacy-ipop/ipop-tap/src/translator.h',
        '../legacy-ipop/ipop-tap/lib/klib/khash.h',
      ],
    },  # target ipop-tap
    {
      'target_name': 'ipop-tincan',
      'type': 'executable',
      'dependencies': [
        'ipop-tap',
      ],
      'sources': [
        '../legacy-ipop/ipop-tincan/src/tincan.cc',
        '../legacy-ipop/ipop-tincan/src/tincanconnectionmanager.cc',
        '../legacy-ipop/ipop-tincan/src/tincanconnectionmanager.h',
        '../legacy-ipop/ipop-tincan/src/xmppnetwork.cc',
        '../legacy-ipop/ipop-tincan/src/xmppnetwork.h',
        '../legacy-ipop/ipop-tincan/src/controlleraccess.cc',
        '../legacy-ipop/ipop-tincan/src/controlleraccess.h',
        '../legacy-ipop/ipop-tincan/src/tincanxmppsocket.cc',
        '../legacy-ipop/ipop-tincan/src/tincanxmppsocket.h',
        '../legacy-ipop/ipop-tincan/src/tincan_utils.h',
        '../legacy-ipop/ipop-tincan/src/tincan_utils.cc',
        '../webrtc/libjingle/xmpp/jingleinfotask.cc',
        '../webrtc/libjingle/xmpp/jingleinfotask.h',
      ],
    },  # target ipop-tincan
  ],
}
