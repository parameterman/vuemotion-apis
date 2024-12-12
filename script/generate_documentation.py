import os
import re

def read_api_files(api_dir='apis'):
    """读取所有API文件内容
    
    Args:
        api_dir (str): API文件所在目录路径，默认为'apis'
        
    Returns:
        list: 包含API文件内容的字典列表
    """
    api_contents = []
    
    # 确保路径存在
    if not os.path.exists(api_dir):
        raise FileNotFoundError(f"API目录 '{api_dir}' 不存在")
    
    for root, _, files in os.walk(api_dir):
        for file in files:
            if file.endswith('.api'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        api_contents.append({
                            'file': file,
                            'content': content
                        })
                except Exception as e:
                    print(f"读取文件 '{file_path}' 时出错: {str(e)}")
    
    if not api_contents:
        print(f"警告: 在 '{api_dir}' 目录中没有找到.api文件")
    
    return api_contents

def parse_docstring(content):
    """解析文件中的文档字符串"""
    # 查找三引号文档字符串
    doc_pattern = r'"""(.*?)"""'
    docs = re.findall(doc_pattern, content, re.DOTALL)
    return docs

def generate_documentation():
    """生成markdown文档"""
    api_contents = read_api_files()
    
    # 创建输出目录
    output_dir = 'docs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 生成markdown文件
    with open(os.path.join(output_dir, 'origindata.md'), 'w', encoding='utf-8') as f:
        for api in api_contents:
            f.write(f'## `{api["file"].replace(".api", "")}`\n\n')
            
            # 解析并写入文档字符串
            docs = parse_docstring(api['content'])
            for doc in docs:
                f.write(f'{doc.strip()}\n\n')
            
            # 添加代码块
            f.write(api['content'])
            f.write('\n\n')
            f.write('---')
            f.write('\n\n')
if __name__ == "__main__":
    generate_documentation()
