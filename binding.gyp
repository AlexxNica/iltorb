{
  "targets": [
    {
      "target_name": "encode",
      "sources": [
        "brotli/enc/backward_references.cc",
        "brotli/enc/block_splitter.cc",
        "brotli/enc/brotli_bit_stream.cc",
        "brotli/enc/dictionary.cc",
        "brotli/enc/encode.cc",
        "brotli/enc/encode_parallel.cc",
        "brotli/enc/entropy_encode.cc",
        "brotli/enc/histogram.cc",
        "brotli/enc/literal_cost.cc",
        "brotli/enc/metablock.cc",
        "brotli/enc/static_dict.cc",
        "brotli/enc/streams.cc",
        "brotli/enc/utf8_util.cc",
        "src/encode.cc"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "cflags" : ["-O2"],
      "xcode_settings": {
        "OTHER_CFLAGS" : ["-O2"]
      }
    },
    {
      "target_name": "decode",
      "sources": [
        "brotli/dec/bit_reader.c",
        "brotli/dec/decode.c",
        "brotli/dec/dictionary.c",
        "brotli/dec/huffman.c",
        "brotli/dec/state.c",
        "brotli/dec/streams.c",
        "src/decode.cc"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "cflags" : ["-O2"],
      "xcode_settings": {
        "OTHER_CFLAGS" : ["-O2"]
      }
    }
  ]
}
