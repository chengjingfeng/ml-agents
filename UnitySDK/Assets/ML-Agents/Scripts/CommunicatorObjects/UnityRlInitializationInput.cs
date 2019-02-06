// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: mlagents_envs/communicator_objects/unity_rl_initialization_input.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace MLAgents.CommunicatorObjects {

  /// <summary>Holder for reflection information generated from mlagents_envs/communicator_objects/unity_rl_initialization_input.proto</summary>
  public static partial class UnityRlInitializationInputReflection {

    #region Descriptor
    /// <summary>File descriptor for mlagents_envs/communicator_objects/unity_rl_initialization_input.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static UnityRlInitializationInputReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CkZtbGFnZW50c19lbnZzL2NvbW11bmljYXRvcl9vYmplY3RzL3VuaXR5X3Js",
            "X2luaXRpYWxpemF0aW9uX2lucHV0LnByb3RvEhRjb21tdW5pY2F0b3Jfb2Jq",
            "ZWN0cyIqChpVbml0eVJMSW5pdGlhbGl6YXRpb25JbnB1dBIMCgRzZWVkGAEg",
            "ASgFQh+qAhxNTEFnZW50cy5Db21tdW5pY2F0b3JPYmplY3RzYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::MLAgents.CommunicatorObjects.UnityRLInitializationInput), global::MLAgents.CommunicatorObjects.UnityRLInitializationInput.Parser, new[]{ "Seed" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class UnityRLInitializationInput : pb::IMessage<UnityRLInitializationInput> {
    private static readonly pb::MessageParser<UnityRLInitializationInput> _parser = new pb::MessageParser<UnityRLInitializationInput>(() => new UnityRLInitializationInput());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<UnityRLInitializationInput> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::MLAgents.CommunicatorObjects.UnityRlInitializationInputReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLInitializationInput() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLInitializationInput(UnityRLInitializationInput other) : this() {
      seed_ = other.seed_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public UnityRLInitializationInput Clone() {
      return new UnityRLInitializationInput(this);
    }

    /// <summary>Field number for the "seed" field.</summary>
    public const int SeedFieldNumber = 1;
    private int seed_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int Seed {
      get { return seed_; }
      set {
        seed_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as UnityRLInitializationInput);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(UnityRLInitializationInput other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Seed != other.Seed) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Seed != 0) hash ^= Seed.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Seed != 0) {
        output.WriteRawTag(8);
        output.WriteInt32(Seed);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Seed != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(Seed);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(UnityRLInitializationInput other) {
      if (other == null) {
        return;
      }
      if (other.Seed != 0) {
        Seed = other.Seed;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 8: {
            Seed = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
